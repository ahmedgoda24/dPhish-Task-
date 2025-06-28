from rest_framework import serializers
import ipaddress

from ipinfo.models import IPAddress

class IPListSerializer(serializers.Serializer):
    ips = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False
    )

    def validate_ips(self, value):
        for ip in value:
            try:
                ipaddress.ip_address(ip)
            except ValueError:
                raise serializers.ValidationError(f"{ip} is not a valid IP address")
        return value


    
class IPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = ['ip_address', 'data_info', 'created_at']