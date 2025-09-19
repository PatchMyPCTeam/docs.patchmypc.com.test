# Add a Cloud Notification

_Applies to: Patch My PC Cloud_

To add a notification in Patch My PC (PMPC) Cloud:

1.  On the **Notifications** page, click **Add Notification** in the header.\\

    ![Clicking “Add Notification” in the header](../../../.gitbook/assets/image-\(1594\).png)
2.  On the **Add Notifications** screen, enter a unique name for this notification in the **Name** field.\\

    ![Enter a unique name for this notification in the “Name” field](../../../.gitbook/assets/image-\(1598\).png)
3.  If you have more than one environment (in other words, your portal is connected to more than one Intune tenant), select the relevant environment from the **Select Environments** dropdown.\\

    ![Select the relevant environment from the “Select Environments” dropdown](../../../.gitbook/assets/image-\(1599\).png)
4. Follow the relevant process for the type of notification you are creating:

* [Create a Webhook notification](create-a-webhook-notification-in-cloud.md)
* [Create an Email notification](create-a-cloud-email-notification.md)

{% hint style="info" %}
**Note**

Given [Microsoft's announcement](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) to retire Office 365 connectors (which includes Webhooks), we are already working on a Workflow solution that will be available well in advance of Microsoft's retirement plans. Stay tuned for updates.
{% endhint %}
