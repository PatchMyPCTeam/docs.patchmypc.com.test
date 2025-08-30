# Delete an App Registration in Entra ID

_Applies to: Patch My PC Cloud_

Once you have successfully completed any scenarios (such as [Recover Your Company](../../cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md)) where you had to create an App Registration for use in Patch My PC (PMPC) Cloud, you need to delete the App Registration to avoid potential security issues and prevent unwanted re-use.

To delete an App Registration:

1. Sign in to the Microsoft Azure portal using an account with the **GlobalAdmin** role and navigate to the [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) blade.

{% hint style="warning" %}
**Important**

You must use an account in the same Microsoft 365 subscription (tenant) as your PMPC Company.
{% endhint %}

![Navigating to the “App registrations” blade](../../../_images/image%20%281970%29.png%20"Navigating%20to%20the%20\"App%20registrations\"%20blade")

2.  Click **All applications**.\


    ![Clicking “All Applications”](../../../_images/image%20%281971%29.png%20"Clicking%20\"All%20Applications\"")

    \

3.  Click the **PMPC Recovery** application.\


    ![Clicking the “PMPC Recovery” application](../../../_images/image%20%281972%29.png%20"Clicking%20the%20\"PMPC%20Recovery\"%20application")

    \


    4.  Click **Delete**.\


        ![Clicking “Delete”](../../../_images/image%20%281973%29.png%20"Clicking%20\"Delete\"")

        \

    5.  On the **Delete app registration** screen, check the **I understand the implications of deleting this app registration** checkbox, then click **Delete**.\
        \


        ![Checking the “I understand the implications of deleting this app registration” checkbox, then clicking “Delete”.](../../../_images/image%20%281974%29.png%20"Checking%20the%20\"I%20understand%20the%20implications%20of%20deleting%20this%20app%20registration\"%20checkbox,%20then%20clicking%20\"Delete\".")

        \
        The **Welcome to Azure** page is shown and the **Delete application - Successfully deleted application PMPC Recovery** notification is shown.\
        \


        ![“App registrations” page refreshes and the “Delete application - Successfully deleted application PMPC Recovery” notification is shown.](../../../_images/image%20%281975%29.png%20"\"App%20registrations\"%20page%20refreshes%20and%20the%20\"Delete%20application%20-%20Successfully%20deleted%20application%20PMPC%20Recovery\"%20notification%20is%20shown.")

        \

    6.  Click **App Registrations**.\
        \


        ![Clicking the “App Registrations” blade](../../../_images/image%20%281976%29.png%20"Clicking%20the%20\"App%20Registrations\"%20blade")

        \

    7.  On the **App registrations** screen, click **All applications**.\
        \


        ![Clicking the “All applications” blade](../../../_images/image%20%281977%29.png%20"Clicking%20the%20\"All%20applications\"%20blade")

        \

    8.  Verify the **PMPC Recovery** application has been deleted.\
        \


        ![Verifying the “PMPC Recovery” application has been deleted.](../../../_images/image%20%281978%29.png%20"Verifying%20the%20\"PMPC%20Recovery\"%20application%20has%20been%20deleted.")
