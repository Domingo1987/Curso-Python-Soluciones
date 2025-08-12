import requests
from bs4 import BeautifulSoup
import csv
import re
import time
from datetime import datetime

def extraer_articulo(numero):
    """
    Extrae un artículo específico de la Constitución de Uruguay
    """
    base_url = "https://www.impo.com.uy/bases/constitucion/1967-1967"
    url = f"{base_url}/{numero}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Inicializar variables
        fecha = ""
        articulo_num = f"Artículo {numero}"
        descripcion = ""
        notas = ""
        
        # 1. EXTRAER FECHA
        # Buscar patrón: <h5>Fecha de Publicación: DD/MM/YYYY </h5>
        fecha_element = soup.find('h5', string=re.compile(r'Fecha de Publicación', re.IGNORECASE))
        if fecha_element:
            fecha_texto = fecha_element.get_text()
            match_fecha = re.search(r'(\d{2}/\d{2}/\d{4})', fecha_texto)
            if match_fecha:
                fecha = match_fecha.group(1)
        
        # Si no encuentra en h5, buscar en cualquier lugar
        if not fecha:
            fecha_general = soup.find(text=re.compile(r'Fecha de Publicación.*?\d{2}/\d{2}/\d{4}', re.IGNORECASE))
            if fecha_general:
                match_fecha = re.search(r'(\d{2}/\d{2}/\d{4})', fecha_general)
                if match_fecha:
                    fecha = match_fecha.group(1)
        
        # 2. EXTRAER TÍTULO DEL ARTÍCULO
        # Buscar <h4 class="resultado">Artículo X</h4>
        titulo_element = soup.find('h4', {'class': 'resultado'})
        if titulo_element:
            titulo_texto = titulo_element.get_text().strip()
            if 'Artículo' in titulo_texto:
                articulo_num = titulo_texto
        
        # 3. EXTRAER DESCRIPCIÓN
        # Buscar el <pre> que viene después del h4 del artículo
        if titulo_element:
            descripcion_element = titulo_element.find_next_sibling('pre')
            if descripcion_element:
                descripcion = descripcion_element.get_text().strip()
                # Limpiar espacios extra
                descripcion = re.sub(r'\s+', ' ', descripcion)
        
        # Si no encuentra descripción con el método anterior, buscar por patrón
        if not descripcion:
            # Buscar todos los <pre> y encontrar el que contiene el texto del artículo
            pre_elements = soup.find_all('pre')
            for pre in pre_elements:
                texto = pre.get_text().strip()
                # Verificar que no sea una nota (no contiene "Notas:" o asteriscos al inicio)
                if (texto and 
                    len(texto) > 20 and 
                    not re.match(r'^\(\*\)', texto) and 
                    'Notas:' not in texto and
                    'Ver en esta norma' not in texto):
                    descripcion = re.sub(r'\s+', ' ', texto)
                    break
        
        # 4. EXTRAER NOTAS
        # Buscar <pre class="italica"> que contiene las notas
        notas_elements = soup.find_all('pre', {'class': 'italica'})
        notas_lista = []
        
        for nota_element in notas_elements:
            nota_texto = nota_element.get_text().strip()
            
            # Filtrar líneas de separación (solo guiones o asteriscos)
            if re.match(r'^[\-\*\(\)]*$', nota_texto):
                continue
                
            # Limpiar formato de notas
            nota_texto = re.sub(r'^\(\*\)\s*', '', nota_texto)  # Remover (*) al inicio
            nota_texto = re.sub(r'^Notas:\s*', '', nota_texto, flags=re.IGNORECASE)  # Remover "Notas:"
            nota_texto = re.sub(r'\s+', ' ', nota_texto)  # Limpiar espacios
            
            if nota_texto and len(nota_texto) > 3:
                notas_lista.append(nota_texto)
        
        # También buscar notas en elementos que contengan "Ver en esta norma" o enlaces
        enlaces_notas = soup.find_all(text=re.compile(r'Ver en esta norma|artículo:', re.IGNORECASE))
        for enlace in enlaces_notas:
            parent = enlace.parent
            if parent:
                nota_texto = parent.get_text().strip()
                nota_texto = re.sub(r'\s+', ' ', nota_texto)
                if nota_texto and nota_texto not in notas_lista:
                    notas_lista.append(nota_texto)
        
        # Unir todas las notas
        notas = ' | '.join(notas_lista) if notas_lista else ""
        
        # Validar que tenemos información útil
        if not descripcion or len(descripcion) < 10:
            print(f"⚠️  Artículo {numero}: descripción muy corta o vacía")
            return None
            
        return {
            'fecha': fecha,
            'articulo': articulo_num,
            'descripcion': descripcion,
            'notas': notas
        }
        
    except requests.RequestException as e:
        print(f"❌ Error de conexión en artículo {numero}: {e}")
        return None
    except Exception as e:
        print(f"❌ Error procesando artículo {numero}: {e}")
        return None

def extraer_constitucion_completa():
    """
    Extrae todos los artículos de la Constitución de Uruguay (1-332)
    """
    articulos = []
    errores = []
    
    print("🇺🇾 Iniciando extracción de la Constitución de Uruguay...")
    print("📄 Extrayendo: fecha, artículo, descripción y notas")
    print("⏱️  Esto puede tomar varios minutos...\n")
    
    # Rango de artículos (1 a 332)
    for numero in range(1, 333):
        print(f"📖 Procesando artículo {numero:3d}/332...", end=' ')
        
        articulo = extraer_articulo(numero)
        
        if articulo:
            articulos.append(articulo)
            print("✅")
        else:
            errores.append(numero)
            print("❌")
        
        # Pausa para no sobrecargar el servidor
        time.sleep(0.8)
        
        # Mostrar progreso cada 25 artículos
        if numero % 25 == 0:
            porcentaje = (numero / 332) * 100
            print(f"\n📊 Progreso: {numero}/332 ({porcentaje:.1f}%)")
            print(f"✅ Extraídos: {len(articulos)} | ❌ Errores: {len(errores)}\n")
    
    print(f"\n{'='*60}")
    print(f"🎯 RESUMEN FINAL:")
    print(f"📝 Total artículos procesados: 332")
    print(f"✅ Artículos extraídos exitosamente: {len(articulos)}")
    print(f"❌ Artículos con errores: {len(errores)}")
    
    if errores:
        print(f"🔍 Artículos problemáticos: {errores[:15]}{'...' if len(errores) > 15 else ''}")
    
    # Guardar resultados en CSV
    if articulos:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f'constitucion_uruguay_{timestamp}.csv'
        
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['fecha', 'articulo', 'descripcion', 'notas']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for articulo in articulos:
                writer.writerow(articulo)
        
        print(f"\n💾 Datos guardados en: {nombre_archivo}")
        
        # Mostrar muestra de los primeros artículos
        print(f"\n{'='*60}")
        print("📋 MUESTRA DE ARTÍCULOS EXTRAÍDOS:")
        for i, art in enumerate(articulos[:3]):
            print(f"\n📅 Fecha: {art['fecha']}")
            print(f"📄 {art['articulo']}")
            print(f"📝 Descripción: {art['descripcion'][:150]}{'...' if len(art['descripcion']) > 150 else ''}")
            if art['notas']:
                print(f"📌 Notas: {art['notas'][:100]}{'...' if len(art['notas']) > 100 else ''}")
            print("-" * 40)
        
        # Estadísticas detalladas
        print(f"\n{'='*60}")
        print("📈 ESTADÍSTICAS DETALLADAS:")
        
        # Artículos con fecha
        articulos_con_fecha = sum(1 for art in articulos if art['fecha'])
        print(f"📅 Artículos con fecha: {articulos_con_fecha}/{len(articulos)}")
        
        # Artículos con notas
        articulos_con_notas = sum(1 for art in articulos if art['notas'])
        print(f"📌 Artículos con notas: {articulos_con_notas}/{len(articulos)}")
        
        # Longitudes de descripción
        longitudes = [len(art['descripcion']) for art in articulos if art['descripcion']]
        if longitudes:
            print(f"📏 Longitud promedio descripción: {sum(longitudes) // len(longitudes)} caracteres")
            print(f"📏 Descripción más larga: {max(longitudes)} caracteres")
            print(f"📏 Descripción más corta: {min(longitudes)} caracteres")
        
        # Fechas únicas
        fechas_unicas = set(art['fecha'] for art in articulos if art['fecha'])
        print(f"📆 Fechas de publicación encontradas: {len(fechas_unicas)}")
        if fechas_unicas:
            print(f"📆 Fechas: {sorted(fechas_unicas)}")
        
    else:
        print("\n❌ No se pudieron extraer artículos. Verifica la conexión y la estructura del sitio.")
    
    return articulos, errores

def reintentar_errores(numeros_error):
    """
    Reintenta extraer artículos que fallaron en el primer intento
    """
    if not numeros_error:
        return []
    
    print(f"\n🔄 Reintentando {len(numeros_error)} artículos que fallaron...")
    articulos_recuperados = []
    
    for numero in numeros_error:
        print(f"🔄 Reintentando artículo {numero}...", end=' ')
        time.sleep(2)  # Pausa más larga para reintentos
        
        articulo = extraer_articulo(numero)
        if articulo:
            articulos_recuperados.append(articulo)
            print("✅")
        else:
            print("❌")
    
    print(f"🎯 Artículos recuperados en el reintento: {len(articulos_recuperados)}")
    return articulos_recuperados

if __name__ == "__main__":
    print("🚀 EXTRACTOR DE CONSTITUCIÓN DE URUGUAY")
    print("=" * 60)
    
    # Extraer todos los artículos
    articulos, errores = extraer_constitucion_completa()
    
    # Reintentar artículos que fallaron
    if errores and len(errores) <= 20:  # Solo reintentar si hay pocos errores
        respuesta = input(f"\n❓ ¿Deseas reintentar los {len(errores)} artículos que fallaron? (s/n): ")
        if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            articulos_recuperados = reintentar_errores(errores)
            
            if articulos_recuperados:
                # Agregar artículos recuperados al CSV más reciente
                import glob
                archivos_csv = glob.glob('constitucion_uruguay_*.csv')
                if archivos_csv:
                    archivo_mas_reciente = max(archivos_csv)
                    with open(archivo_mas_reciente, 'a', newline='', encoding='utf-8') as csvfile:
                        fieldnames = ['fecha', 'articulo', 'descripcion', 'notas']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        for articulo in articulos_recuperados:
                            writer.writerow(articulo)
                    
                    print(f"✅ Se agregaron {len(articulos_recuperados)} artículos recuperados al CSV.")
    
    print(f"\n🎉 ¡Proceso completado!")
    print("📁 Revisa el archivo CSV generado para ver todos los artículos extraídos.")