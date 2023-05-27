# DPhi-Assignment

### Register User (/user/register/)
```
Post Request
{
    "username": "test",
    "password": "test",
    "email" : "test@example.com"
}
```
![image](https://github.com/dhruva3223/DPhi-Assignment/assets/91244148/6ba47930-0292-44fb-8ab8-2c72b4d5409a)

### Login User (/user/login/)
```
Post Request
{
    "username": "test",
    "password": "test"
}
```
![image](https://github.com/dhruva3223/DPhi-Assignment/assets/91244148/63125557-2906-44e9-92d9-90e80fc02cc6)

### View Hackathon List (hackathon/hackathons/)

![image](https://github.com/dhruva3223/DPhi-Assignment/assets/91244148/82eaf4f4-f2e7-4c73-a179-6e39ffe881fa)

### View Single Hackathon (hackathon/hackathons/1/)

![image](https://github.com/dhruva3223/DPhi-Assignment/assets/91244148/78d10ad2-b5fd-4ea1-8352-f177c93db2ae)

### Register User in Hackathon (/hackathon/user/hackathons/)
```
Post Request
{
    "user": "3",
    "hackathon": "2"
}
```
![image](https://github.com/dhruva3223/DPhi-Assignment/assets/91244148/debfeda1-a576-43ba-aeb7-a659d528acea)

### View Registered Hackathon of a user (/hackathon/user/hackathons/)

![image](https://github.com/dhruva3223/DPhi-Assignment/assets/91244148/8b2952a4-1206-4fe5-b6fd-c863c3deeb92)

### View Hackathon Submissions of a user (user/hackathons/<int:hackathon_id>/submissions/)
![image](https://github.com/dhruva3223/DPhi-Assignment/assets/91244148/7454a7d7-dd50-43e1-8d83-6d673f4f050b)

### Post Hackathon Submission file/image/link (user/hackathons/<int:hackathon_id>/submissions/)

### Post Hackathon (/hackathon/hackathons/)
