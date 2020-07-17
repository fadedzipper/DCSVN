from rest_framework import serializers
from device import models

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:

        is_active = serializers.IntegerField()
        model = models.Device
        fields = ['id', 'device_id', 'device_name', 'is_active', 'status', 'mac_addr', \
                  'Longitude', 'Latitude', 'info', 'net']

        # device 有可能是不能修改的

        def get_is_active(self, obj):
            if obj.is_active == 0:
                return "离线"
            return "在线"


class DeviceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Device
        fields = ['is_active', 'Longitude', 'Latitude', 'net', 'info', 'is_active']


class DeviceUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = ['id', 'is_active']
