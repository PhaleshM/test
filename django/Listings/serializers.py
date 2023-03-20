from rest_framework import serializers
from .models import Listing,ListingImage
from account.utils import Util


class ListingImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = "__all__"

class ListingSerializers(serializers.ModelSerializer):
    images =  ListingImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Listing
        fields = ["id", "name","user","product", "description","ratecriteria", "rate", "date", "images",
                  "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        listing = Listing.objects.create(**validated_data)
        for image in uploaded_images:
            ListingImage.objects.create(name=listing, image=image)

        return listing
