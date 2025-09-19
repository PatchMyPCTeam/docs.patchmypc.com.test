# Manage Cloud Notifications

_Applies to: Patch My PC Cloud_

Once onboarded to Patch My PC (PMPC) Cloud, you can use the **Notifications** node to configure notifications to be sent from the portal to:

* Microsoft Teams
* Slack
* Email addresses

{% hint style="info" %}
**Note**

If configured and regardless of whether or not the deployment uses Update Rings, we send Slack/webhook notifications whenever:

* A new deployment is created.
* The version of an existing deployment is updated.
* A new Update Ring is created.
* An existing Update Ring is upgraded to a later version
* An admin clicks [Sync Now](../../cloud-deployments/manage-updates-in-cloud/sync-now-cloud-feature.md) to force a deployment to update immediately to the latest version without waiting for the Sync Schedule to run.

Provided you have configured an [email notification](create-a-cloud-email-notification.md), six hours after your [Sync Schedule](../manage-the-sync-schedule-in-cloud.md) has run, the [Updates Report](../../cloud-reference/cloud-email-reference/example-cloud-updates-report-email.md) will be generated and sent to the configured email addresses.

On this report:

* A new deployment appears as **Initial Deployment Created**.
* An existing deployment updated to a newer version appears as **Version Update**.
{% endhint %}

To configure Notifications:

1. Sign in to the portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2.  Navigate to **Settings | Notifications**.\\

    !\[]\(/\_images/image-(760 "").png "")

The **Notifications** page is then displayed, showing any existing Notifications and allowing you to:

* [Add a Notification](add-a-cloud-notification.md)
* [Modify a Notification](modify-a-cloud-notification.md)
* [Delete a Notification](delete-a-cloud-notification.md)

!\[]\(/\_images/image-(761 "").png "")
