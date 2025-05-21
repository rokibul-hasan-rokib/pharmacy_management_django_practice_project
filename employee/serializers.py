from rest_framework import serializers
from .models import Employee, Department, Designation

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'designation', 'status']
        read_only_fields = ['id']



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
        read_only_fields = ['id']

        
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)