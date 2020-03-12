'''The message will be consumed from the queue and according to the type
 1. sms
        hit the sms api: https://api.rmlconnect.net/bulksms/bulksms?username=X&password=Y&type=Y&dlr=Z&destination=Q&source=R&message=S
2. whatsapp
    hit the whatsapp url https://whtsappqa.clickpost.com/api/v1/receiver/push-message
    method: 'post',
                url: CONFIG.SOCIAL_MESSAGING_SERVICE_URL + '/api/v1/receiver/push-message',
                data: data,
                headers: { 'Content-Type': 'application/json'}
'''