# Serializadores en Django Rest Framework (DRF)

## ¿Qué es un Serializador?
Los serializadores en DRF permiten convertir estructuras de datos complejas como modelos de Django en formatos fácilmente legibles (JSON, XML, etc.) y viceversa.

---

## Tipos de Serializadores en DRF
DRF proporciona diferentes tipos de serializadores para distintas necesidades:

### 1. `serializers.Serializer` (Serializador Manual)
Ofrece control total sobre la serialización/deserialización.

#### Ejemplo:
```python
from rest_framework import serializers

class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Usuario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
```

---

### 2. `serializers.ModelSerializer` (Serializador Automático)
Reduce el código repetitivo, generando automáticamente los campos a partir de un modelo de Django.

#### Ejemplo:
```python
from rest_framework import serializers
from .models import Usuario

class UsuarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # También se puede usar ('id', 'nombre', 'email')
```

---

## Validación en Serializadores
Los serializadores en DRF permiten validaciones personalizadas.

### Ejemplo de validación personalizada:
```python
class UsuarioSerializer(serializers.Serializer):
    email = serializers.EmailField()
    edad = serializers.IntegerField()

    def validate_edad(self, value):
        if value < 18:
            raise serializers.ValidationError("La edad debe ser mayor o igual a 18.")
        return value

    def validate(self, data):
        if "admin" in data['email']:
            raise serializers.ValidationError("No se permiten emails con 'admin'.")
        return data
```

---

## Serialización Anidada
Permite incluir objetos relacionados dentro de un serializador.

### Ejemplo:
```python
class DireccionSerializer(serializers.Serializer):
    calle = serializers.CharField(max_length=255)
    ciudad = serializers.CharField(max_length=100)

class UsuarioSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=255)
    direccion = DireccionSerializer()
```

---

## Serializadores y Relaciones
DRF ofrece varias opciones para manejar relaciones entre modelos.

### `PrimaryKeyRelatedField`
```python
class UsuarioSerializer(serializers.ModelSerializer):
    grupo = serializers.PrimaryKeyRelatedField(queryset=Grupo.objects.all())
    
    class Meta:
        model = Usuario
        fields = '__all__'
```

### `StringRelatedField`
```python
class UsuarioSerializer(serializers.ModelSerializer):
    grupo = serializers.StringRelatedField()
    
    class Meta:
        model = Usuario
        fields = '__all__'
```

---

## Serializadores Hiperenlazados
Utiliza URLs en lugar de claves primarias para representar relaciones.

### Ejemplo:
```python
from rest_framework import serializers
from .models import Usuario

class UsuarioHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url', 'id', 'nombre', 'email']
```

---