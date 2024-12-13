from pywebpush import webpush, WebPushException

VAPID_PRIVATE_KEY = "BK9aUMcGay5K18U0I1kNfy18cnrO5j1R22GJ3XiTANUgWgwAxd96pT-ysHVtSxki7A3vrDoYiCHeXx4FjGdiXhU"
VAPID_PUBLIC_KEY = "9yn6zCjO658_v2aE2iIQ_ZhwjmHE95np2FECaTXOTZ8"
VAPID_CLAIMS = {
    "sub": "mailto: <hanzalaomar1@gmail.com"
}



def send_notification(subscription_info, payload):
    try:
        webpush(
            subscription_info=subscription_info,
            data=payload,
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS,
        )
    except WebPushException as ex:
        print("Failed to send push notification: ", repr(ex))
