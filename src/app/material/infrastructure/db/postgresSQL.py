from datetime import datetime
from typing import List, Optional

from src.shared.db.database import get_db
from src.app.material.domain.repository import MaterialRepository
from src.shared.db.orm_models import Material as ORMMaterial, Class
from src.app.material.domain.models import Material, CreateMaterialRequest, UpdateMaterialRequest


class PostgreSQLRepository(MaterialRepository):
    def __init__(self):
        self.connection = next(get_db())
        if not self.connection:
            raise Exception("No database connection")

    async def create(self, material_data: CreateMaterialRequest) -> Material:
        """Crea un nuevo material y retorna el material creado con su ID"""
        try:
            # Verificar que la clase existe
            clazz = (
                self.connection.query(Class)
                .filter(Class.idClass == material_data.idClass)
                .first()
            )
            if not clazz:
                raise Exception(
                    f"Class with ID {material_data.idClass} not found")

            new_material = ORMMaterial(
                idClass=material_data.idClass,
                title=material_data.title,
                description=material_data.description,
                urlFile=material_data.urlFile,
                urlLink=material_data.urlLink,
                createdAt=datetime.utcnow()
            )

            self.connection.add(new_material)
            self.connection.commit()
            self.connection.refresh(new_material)

            return Material(
                idMaterial=new_material.idMaterial,
                idClass=new_material.idClass,
                title=new_material.title,
                description=new_material.description,
                urlFile=new_material.urlFile,
                urlLink=new_material.urlLink
            )

        except Exception as e:
            self.connection.rollback()
            raise e

    async def get_by_id(self, material_id: int) -> Optional[Material]:
        """Obtiene un material por su ID, retorna None si no existe"""
        try:
            material = (
                self.connection.query(ORMMaterial)
                .filter(ORMMaterial.idMaterial == material_id)
                .first()
            )
            if not material:
                return None

            return Material(
                idMaterial=material.idMaterial,
                idClass=material.idClass,
                title=material.title,
                description=material.description,
                urlFile=material.urlFile,
                urlLink=material.urlLink
            )

        except Exception as e:
            raise e

    async def get_by_class_id(self, class_id: int) -> List[Material]:
        """Obtiene todos los materiales de una clase específica"""
        try:
            clazz = (
                self.connection.query(Class)
                .filter(Class.idClass == class_id)
                .first()
            )
            if not clazz:
                raise Exception(f"Class with ID {class_id} not found")

            materials = (
                self.connection.query(ORMMaterial)
                .filter(ORMMaterial.idClass == class_id)
                .order_by(ORMMaterial.createdAt.desc())
                .all()
            )

            return [
                Material(
                    idMaterial=m.idMaterial,
                    idClass=m.idClass,
                    title=m.title,
                    description=m.description,
                    urlFile=m.urlFile,
                    urlLink=m.urlLink
                ) for m in materials
            ]

        except Exception as e:
            raise e

    async def get_by_class_and_material_id(self, class_id: int, material_id: int) -> Optional[Material]:
        """Obtiene un material específico de una clase específica"""
        try:
            material = (
                self.connection.query(ORMMaterial)
                .filter(
                    ORMMaterial.idMaterial == material_id,
                    ORMMaterial.idClass == class_id
                )
                .first()
            )
            if not material:
                return None

            return Material(
                idMaterial=material.idMaterial,
                idClass=material.idClass,
                title=material.title,
                description=material.description,
                urlFile=material.urlFile,
                urlLink=material.urlLink
            )

        except Exception as e:
            raise e

    async def update(self, material_id: int, class_id: int, update_data: UpdateMaterialRequest) -> Optional[Material]:
        """Actualiza un material y retorna el material actualizado"""
        try:
            material = (
                self.connection.query(ORMMaterial)
                .filter(
                    ORMMaterial.idMaterial == material_id,
                    ORMMaterial.idClass == class_id
                )
                .first()
            )
            if not material:
                return None

            # Actualizar solo los campos proporcionados
            for key, value in update_data.dict(exclude_unset=True).items():
                setattr(material, key, value)

            self.connection.commit()
            self.connection.refresh(material)

            return Material(
                idMaterial=material.idMaterial,
                idClass=material.idClass,
                title=material.title,
                description=material.description,
                urlFile=material.urlFile,
                urlLink=material.urlLink
            )

        except Exception as e:
            self.connection.rollback()
            raise e

    async def delete(self, material_id: int, class_id: int) -> bool:
        """Elimina un material por su ID y clase, retorna True si se eliminó"""
        try:
            material = (
                self.connection.query(ORMMaterial)
                .filter(
                    ORMMaterial.idMaterial == material_id,
                    ORMMaterial.idClass == class_id
                )
                .first()
            )
            if not material:
                return False

            self.connection.delete(material)
            self.connection.commit()
            return True

        except Exception as e:
            self.connection.rollback()
            raise e

    async def get_materials_by_asignature(self, asignature_id: int) -> List[Material]:
        """Obtiene todos los materiales de todas las clases de una asignatura"""
        try:
            classes = (
                self.connection.query(Class)
                .filter(Class.idAsignature == asignature_id)
                .all()
            )
            materials = []
            for clazz in classes:
                class_materials = (
                    self.connection.query(ORMMaterial)
                    .filter(ORMMaterial.idClass == clazz.idClass)
                    .order_by(ORMMaterial.createdAt.desc())
                    .all()
                )
                for m in class_materials:
                    materials.append(
                        Material(
                            idMaterial=m.idMaterial,
                            idClass=m.idClass,
                            title=m.title,
                            description=m.description,
                            urlFile=m.urlFile,
                            urlLink=m.urlLink
                        )
                    )
            return materials

        except Exception as e:
            raise e
