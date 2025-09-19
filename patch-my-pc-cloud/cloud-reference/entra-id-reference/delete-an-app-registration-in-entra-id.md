# Delete an App Registration in Entra ID

_Applies to: Patch My PC Cloud_

Once you have successfully completed any scenarios (such as [Recover Your Company](../../cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md)) where you had to create an App Registration for use in Patch My PC (PMPC) Cloud, you need to delete the App Registration to avoid potential security issues and prevent unwanted re-use.

To delete an App Registration:

1. Sign in to the Microsoft Azure portal using an account with the **GlobalAdmin** role and navigate to the [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) blade.

{% hint style="warning" %}
**Important**

You must use an account in the same Microsoft 365 subscription (tenant) as your PMPC Company.
{% endhint %}

![Navigating to the “App registrations” blade](../../../.gitbook/assets/image-\(1970\).png)

2.  Click **All applications**.\\

    ![Clicking “All Applications”](../../../.gitbook/assets/image-\(1971\).png)

    \\
3.  Click the **PMPC Recovery** application.\\

    ![Clicking the “PMPC Recovery” application](../../../.gitbook/assets/image-\(1972\).png)

    \\

    4.  Click **Delete**.\\

        ![Clicking “Delete”](../../../.gitbook/assets/image-\(1973\).png)

        \\
    5.  On the **Delete app registration** screen, check the **I understand the implications of deleting this app registration** checkbox, then click **Delete**.\
        \\

        ![Checking the “I understand the implications of deleting this app registration” checkbox, then clicking “Delete”.](../../../.gitbook/assets/image-\(1974\).png)

        \
        The **Welcome to Azure** page is shown and the **Delete application - Successfully deleted application PMPC Recovery** notification is shown.\
        \\

        ![“App registrations” page refreshes and the “Delete application - Successfully deleted application PMPC Recovery” notification is shown.](../../../.gitbook/assets/image-\(1975\).png)

        \\
    6.  Click **App Registrations**.\
        \\

        ![Clicking the “App Registrations” blade](../../../.gitbook/assets/image-\(1976\).png)

        \\
    7.  On the **App registrations** screen, click **All applications**.\
        \\

        ![Clicking the “All applications” blade](../../../.gitbook/assets/image-\(1977\).png)

        \\
    8.  Verify the **PMPC Recovery** application has been deleted.\
        \\

        ![Verifying the “PMPC Recovery” application has been deleted.](../../../.gitbook/assets/image-\(1978\).png)
