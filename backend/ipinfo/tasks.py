from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import requests
import logging
from ipinfo.models import IPAddress

logger = logging.getLogger(__name__)

def send_ip_notification(ip, data):
    """
    Send a notification about the IP address data.
    This function can be used to send notifications via email, SMS, etc.
    Currently, it just logs the information.
    """
    logger.info(f"IP: {ip}, Data: {data}")
    # Implement actual notification logic here if needed
    channel_layer= get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "ip_updates",
        {
            "type": "ip.update",
            "ip": ip,
            "data": data,
        }
    )

@shared_task
def process_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}

    obj, _ = IPAddress.objects.update_or_create(
        ip_address=ip,
        defaults={"data_info": data}
    )

    send_ip_notification(ip, data)
    


@shared_task
def fetch_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        response.raise_for_status()
        data = response.json()
        ip_obj = IPAddress(ip_address=ip,data_info=data)
        ip_obj.save()
        print("data saved")
        logger.info(f"Created for {ip}")
        return data
      

    except Exception as e:
        logger.error(f"Failed to fetch info for {ip}: {e}")
        return {'ip': ip, 'error': str(e)}





    



