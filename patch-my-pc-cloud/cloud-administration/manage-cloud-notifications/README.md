# Manage Cloud Notifications

_Applies to: Patch My PC Cloud_

Once onboarded to Patch My PC (PMPC) Cloud, you can use the **Notifications** node to configure notifications to be sent from the portal to:

* Microsoft Teams
* Slack
* Email addresses

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>If configured and regardless of whether or not the deployment uses Update Rings, we send Slack/webhook notifications whenever:</p>
<p>* A new deployment is created.</p>
<p>* The version of an existing deployment is updated.</p>
<p>* A new Update Ring is created.</p>
<p>* An existing Update Ring is upgraded to a later version</p>
<p>* An admin clicks [Sync Now](../../cloud-deployments/manage-updates-in-cloud/sync-now-cloud-feature.md) to force a deployment to update immediately to the latest version without waiting for the Sync Schedule to run.</p>
<p>Provided you have configured an [email notification](create-a-cloud-email-notification.md), six hours after your [Sync Schedule](../manage-the-sync-schedule-in-cloud.md) has run, the [Updates Report](../../cloud-reference/cloud-email-reference/example-cloud-updates-report-email.md) will be generated and sent to the configured email addresses.</p>
<p>On this report:</p>
<p>* A new deployment appears as **Initial Deployment Created**.</p>
<p>* An existing deployment updated to a newer version appears as **Version Update**.</p>
</blockquote>

To configure Notifications:

1. Sign in to the portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/).
2.  Navigate to **Settings | Notifications**.\


    ![Navigating to "Settings | Notifications"](/_images/image-(760).png "Navigating to “Settings | Notifications”")

The **Notifications** page is then displayed, showing any existing Notifications and allowing you to:

* [Add a Notification](add-a-cloud-notification.md)
* [Modify a Notification](modify-a-cloud-notification.md)
* [Delete a Notification](delete-a-cloud-notification.md)

!["Notifications" page](/_images/image-(761).png "“Notifications” page")