import csv
import sys
from pathlib import Path


def exportar_csv_a_md(archivo_csv, archivo_md):
    """Convierte un archivo CSV a una tabla Markdown."""
    with open(archivo_csv, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        filas = list(reader)

    if not filas:
        return

    encabezados = '| ' + ' | '.join(filas[0]) + ' |\n'
    separador = '| ' + ' | '.join(['---'] * len(filas[0])) + ' |\n'
    lineas = [encabezados, separador]

    for fila in filas[1:]:
        lineas.append('| ' + ' | '.join(fila) + ' |\n')

    Path(archivo_md).write_text(''.join(lineas), encoding='utf-8')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Uso: python exportar_calificaciones.py datos.csv salida.md')
        sys.exit(1)
    exportar_csv_a_md(sys.argv[1], sys.argv[2])
