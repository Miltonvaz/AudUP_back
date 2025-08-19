from sqlalchemy import (
    Column, BigInteger, String, Text, Enum, Boolean, ForeignKey, TIMESTAMP
)
from sqlalchemy.orm import relationship, declarative_base
import enum
from sqlalchemy import text

Base = declarative_base()


class UserRole(str, enum.Enum):
    teacher = "teacher"
    student = "student"


class User(Base):
    __tablename__ = "User"

    idUser = Column(BigInteger, primary_key=True, autoincrement=True)
    idRol = Column(Enum(UserRole, name="user_role"), nullable=False)
    firstName = Column(String(255), nullable=False)
    secondName = Column(String(255))
    paternalLastName = Column(String(255), nullable=False)
    maternalLastName = Column(String(255))
    urlProfile = Column(Text)
    email = Column(String(320), unique=True, nullable=False)
    passwordHash = Column(String(255), nullable=False)
    created_at = Column("createdAt", TIMESTAMP(timezone=True), server_default=text("now()"))

    # Relaciones
    asignatures = relationship("Asignature", back_populates="teacher", foreign_keys="Asignature.idTeacher")
    user_asignatures = relationship("UserAsignature", back_populates="user")


class Advertisement(Base):
    __tablename__ = "Advertisement"

    idAdvertisement = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500))

    asignatures = relationship("Asignature", back_populates="advertisement")


class Asignature(Base):
    __tablename__ = "Asignature"

    idAsignature = Column(BigInteger, primary_key=True, autoincrement=True)
    idTeacher = Column(BigInteger, ForeignKey("User.idUser"), nullable=False)
    idAdvertisement = Column(BigInteger, ForeignKey("Advertisement.idAdvertisement"))
    urlBackground = Column(Text)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    created_at = Column("createdAt", TIMESTAMP(timezone=True), server_default=text("now()"))
    linkCode = Column(String(8),nullable = False,unique=True, server_default=text("generate_uuid8()"))

    # Relaciones
    teacher = relationship("User", back_populates="asignatures", foreign_keys=[idTeacher])
    advertisement = relationship("Advertisement", back_populates="asignatures")
    user_asignatures = relationship("UserAsignature", back_populates="asignature")
    classes = relationship("Class", back_populates="asignature")


class UserAsignature(Base):
    __tablename__ = "UserAsignature"

    idUserAsignature = Column(BigInteger, primary_key=True, autoincrement=True)
    idUser = Column(BigInteger, ForeignKey("User.idUser", ondelete="CASCADE"), nullable=False)
    idAsignature = Column(BigInteger, ForeignKey("Asignature.idAsignature", ondelete="CASCADE"), nullable=False)
    enrolledAt = Column(TIMESTAMP, server_default=text("NOW()"))
    isActive = Column(Boolean, server_default="true")

    # Relaciones
    user = relationship("User", back_populates="user_asignatures")
    asignature = relationship("Asignature", back_populates="user_asignatures")


class Class(Base):
    __tablename__ = "Class"

    idClass = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    datetime = Column(TIMESTAMP, nullable=False)
    idAsignature = Column(BigInteger, ForeignKey("Asignature.idAsignature"), nullable=False)

    asignature = relationship("Asignature", back_populates="classes")
    materials = relationship("Material", back_populates="class_")
    transcriptions = relationship("Transcription", back_populates="class_")


class Material(Base):
    __tablename__ = "Material"

    idMaterial = Column(BigInteger, primary_key=True, autoincrement=True)
    idClass = Column(BigInteger, ForeignKey("Class.idClass"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(500))
    urlFile = Column(Text, nullable=False)

    class_ = relationship("Class", back_populates="materials")


class Transcription(Base):
    __tablename__ = "Transcription"

    idTranscription = Column(BigInteger, primary_key=True, autoincrement=True)
    idClass = Column(BigInteger, ForeignKey("Class.idClass"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)

    class_ = relationship("Class", back_populates="transcriptions")
