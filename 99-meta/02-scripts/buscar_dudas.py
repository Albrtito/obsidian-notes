import os
from pathlib import Path
import re
import yaml

class DudasAnalyzer:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.atomic_folder = self.vault_path / "02-Atomic"
        self.output_folder = self.vault_path / "99-Meta" / "2. Scripts" / "Dudas"
        
        # Asegurar que existe el directorio de salida
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def get_asignatura_input(self):
        """Solicita al usuario la asignatura a analizar"""
        asignatura = input("¿De qué asignatura quieres obtener las dudas? (Escribe 'todas' para analizar todas): ").strip()
        return asignatura

    def get_all_asignaturas(self):
        """Obtiene todas las asignaturas disponibles buscando hashtags en los archivos"""
        asignaturas = set()
        for file in self.atomic_folder.glob("**/*.md"):
            with open(file, 'r', encoding='utf-8') as f:
                # Leer todo el contenido
                content = f.read()
                
                # Extraer frontmatter YAML
                try:
                    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                    if frontmatter_match:
                        frontmatter = yaml.safe_load(frontmatter_match.group(1))
                        # Extraer tags del frontmatter si existen
                        if 'tags' in frontmatter:
                            tags = frontmatter['tags']
                            if isinstance(tags, list):
                                asignaturas.update(tags)
                            elif isinstance(tags, str):
                                asignaturas.add(tags)
                except: # Ignorar errores en YAML  
                    pass

                # Extraer tags del contenido (por si no están en frontmatter)
                tags_in_content = re.findall(r'#([A-Za-z0-9]+)(?!\w)', content)
                asignaturas.update([tag for tag in tags_in_content if tag != 'Duda'])
                
                asignaturas.discard('Duda')

        print("Asignaturas encontradas:", asignaturas)
        return list(asignaturas)

    def find_notes_with_tag(self, tag):
        """Encuentra todas las notas que contienen un hashtag específico"""
        matching_files = []
        for file in self.atomic_folder.glob("**/*.md"):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Primero revisar el frontmatter YAML
                try:
                    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                    if frontmatter_match:
                        frontmatter = yaml.safe_load(frontmatter_match.group(1))
                        # Comprobar tags en frontmatter
                        if 'tags' in frontmatter:
                            tags = frontmatter['tags']
                            if isinstance(tags, list) and tag in tags:
                                matching_files.append(file)
                                continue
                            elif isinstance(tags, str) and tag == tags:
                                matching_files.append(file)
                                continue
                except: # Ignorar errores en YAML 
                    pass
                # Luego revisar el contenido del archivo
                if f"#{tag}" in content:
                    matching_files.append(file)
        return matching_files

    def extract_dudas(self, file):
        """Extrae las dudas de un archivo específico"""
        dudas = []
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            for line in lines:
                if '#Duda' in line:
                    # Elimina el hashtag #Duda y cualquier otro hashtag
                    duda = re.sub(r'#[A-Za-z0-9]+', '', line).strip()
                    # Crear un link relativo a la nota
                    note_link = f"[[{file.stem}]]"
                    dudas.append((duda, note_link))
        return dudas

    def create_dudas_file(self, asignatura, dudas):
        """Crea un archivo markdown con las dudas encontradas"""
        output_file = self.output_folder / f"Dudas-{asignatura}.md"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # Título
            f.write(f"# Dudas {asignatura}\n\n")
            
            # Escribir cada duda con su callout
            for i, (duda, note_link) in enumerate(dudas, 1):
                # Callout de la duda
                f.write(f"> [!duda] Duda {i}\n")
                f.write(f"> {duda}\n")
                f.write(f"> Encontrada en: {note_link}\n\n")
                
                # Callout de la solución
                f.write(f"> [!check] Solución {i}\n")
                f.write("> \n\n")  # Espacio en blanco para la solución

    def analyze_asignatura(self, asignatura):
        """Analiza las dudas para una asignatura específica"""
        print(f"Analizando dudas para: {asignatura}")
        
        # Encontrar notas con el hashtag de la asignatura
        matching_files = self.find_notes_with_tag(asignatura)
        
        # Extraer todas las dudas
        all_dudas = []
        for file in matching_files:
            dudas = self.extract_dudas(file)
            all_dudas.extend(dudas)
        
        # Crear archivo de dudas si se encontró alguna
        if all_dudas:
            self.create_dudas_file(asignatura, all_dudas)
            print(f"Se encontraron {len(all_dudas)} dudas para {asignatura}")
        else:
            print(f"No se encontraron dudas para {asignatura}")

    def run(self):
        """Ejecuta el análisis completo"""
        asignatura = self.get_asignatura_input()
        
        if asignatura == 'todas':
            asignaturas = self.get_all_asignaturas()
            print(f"Asignaturas encontradas: {', '.join(asignaturas)}")
            for asig in asignaturas:
                self.analyze_asignatura(asig)
        else:
            self.analyze_asignatura(asignatura)

# Ejemplo de uso
if __name__ == "__main__":
    # Ajusta esta ruta a la ubicación de tu vault de Obsidian
    vault_path = "../../"
    analyzer = DudasAnalyzer(vault_path)
    analyzer.run()
