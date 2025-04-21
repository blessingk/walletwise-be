import httpx

async def send_lead_to_partner(user_data, partner):
    try:
        response = await httpx.post(partner.webhook_url, json=user_data)
        return response.status_code, response.json()
    except Exception as e:
        return 500, {"error": str(e)}
