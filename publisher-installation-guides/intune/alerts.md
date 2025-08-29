---
description: >-
  Getting notified when there are new updates available to deploy, or when
  something doesn't quite go as expected.
---

# Alerts

_Applies to: On-premises Publisher_

To keep you informed when new updates are ready for deployment in your environment, we provide three different ways to get notifications in your environment:

* [Email report via SMTP relay](https://patchmypc.com/how-publishing-alerts-work#topic1)
* [Teams Webhook notification](https://patchmypc.com/how-publishing-alerts-work#topic2)
* [Slack Webhook notification](https://patchmypc.com/how-publishing-alerts-work#topic4)

## SMTP

Configurations for SMTP can vary greatly between environments, use the image below as a reference for your environment.

<figure><img src="../../_images/gitbook/image (1164).png" alt=""><figcaption><p>Basic SMTP Configuration</p></figcaption></figure>

1. Select a Common Provider if applicable
2. Enable The feature to send e-mails
3. Specify YOUR sender e-mail
4. Specify who should receive the e-mail&#x20;
5. Configure Email Authentication
6. Provide login details as needed, and security port details&#x20;

If you have issues setting up SMTP emails, check out our troubleshooting guide below.

{% embed url="https://patchmypc.com/troubleshooting-smtp-email-sending" %}
SMTP email troubleshooting
{% endembed %}

## Teams Webhook

The Microsoft Teams webhook is a simple way to get a notification for each application as it is prepared for your environment. Simply create a new connector in teams, and paste the Web URL into the field.&#x20;

<figure><img src="../../_images/gitbook/image (1117).png" alt=""><figcaption></figcaption></figure>

Need help creating the webhook in teams? No problem, check out our complete guide to creating a Teams webhook.&#x20;

{% embed url="https://patchmypc.com/how-publishing-alerts-work#topic3" %}

## Slack Webhook

The Slack webhook is another simple way to get a notification for each application as it is prepared for your environment. Simply create a new webhook in Slack, and paste the Web URL into the field.&#x20;

<figure><img src="../../_images/gitbook/image (1081).png" alt=""><figcaption></figcaption></figure>

Need help creating the webhook for Slack? No problem, check out our complete guide to creating a Slack webhook.&#x20;

{% embed url="https://patchmypc.com/how-publishing-alerts-work#topic4" %}
