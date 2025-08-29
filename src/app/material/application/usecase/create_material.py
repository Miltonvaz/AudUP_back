from src.app.material.domain.models import Material, CreateMaterialRequest
from src.app.material.domain.repository import MaterialRepository

class CreateMaterial:
    """
    Caso de uso para crear un nuevo material dentro de una clase
    Solo profesores pueden crear materiales
    """
    
    def __init__(self, repository: MaterialRepository):
        self.repository = repository
    
    async def execute(self, material_data: CreateMaterialRequest) -> Material:
        """
        Crear un nuevo material en una clase específica
        El material solo será visible dentro del contexto de esa clase
        
        Args:
            material_data: Datos del material a crear (incluye idClass)
            
        Returns:
            Material: Material creado
            
        Raises:
            ValueError: Si los datos no son válidos
            Exception: Si hay error en la creación
        """
        # Validaciones de negocio
        self._validate_material_data(material_data)
        
        # Crear el material en la clase especificada
        return await self.repository.create(material_data)
    
    def _validate_material_data(self, material_data: CreateMaterialRequest) -> None:
        """Validar datos del material"""
        if not material_data.title or not material_data.title.strip():
            raise ValueError("El título del material no puede estar vacío")
        
        if not material_data.urlFile or not material_data.urlFile.strip():
            raise ValueError("La URL del archivo no puede estar vacía")
        
        if material_data.idClass <= 0:
            raise ValueError("El ID de la clase debe ser un número positivo")
        
        # Validar longitudes
        if len(material_data.title.strip()) > 255:
            raise ValueError("El título del material no puede exceder 255 caracteres")
        
        if material_data.description and len(material_data.description) > 500:
            raise ValueError("La descripción no puede exceder 500 caracteres")