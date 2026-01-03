from rest_framework import serializers
from .models import Folder, File

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ["id", "name"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "folder", "file"]

    def validate_file(self, file):
        allowed = ["pdf", "jpg", "jpeg", "png"]
        ext = file.name.split(".")[-1].lower()

        if ext not in allowed:
            raise serializers.ValidationError("Invalid file type")

        return file

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
