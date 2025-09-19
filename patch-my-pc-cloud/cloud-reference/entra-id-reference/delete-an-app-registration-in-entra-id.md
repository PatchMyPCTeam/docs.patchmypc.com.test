# Delete an App Registration in Entra ID

_Applies to: Patch My PC Cloud_

Once you have successfully completed any scenarios (such as [Recover Your Company](../../cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md)) where you had to create an App Registration for use in Patch My PC (PMPC) Cloud, you need to delete the App Registration to avoid potential security issues and prevent unwanted re-use.

To delete an App Registration:

1. Sign in to the Microsoft Azure portal using an account with the **GlobalAdmin** role and navigate to the [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) blade.

> **Important**
>
> You must use an account in the same Microsoft 365 subscription (tenant) as your PMPC Company.

![Navigating to the "App registrations" blade](/_images/image-(1970 "Navigating to the \"App registrations\" blade").png)

2.  Click **All applications**.\\

    ![Clicking "All Applications"](/_images/image-(1971 "Clicking \"All Applications\"").png)

    \\
3.  Click the **PMPC Recovery** application.\\

    ![Clicking the "PMPC Recovery" application](/_images/image-(1972 "Clicking the \"PMPC Recovery\" application").png)

    \\

    4.  Click **Delete**.\\

        ![Clicking "Delete"](/_images/image-(1973 "Clicking \"Delete\"").png)

        \\
    5.  On the **Delete app registration** screen, check the **I understand the implications of deleting this app registration** checkbox, then click **Delete**.\
        \\

        ![Checking the "I understand the implications of deleting this app registration" checkbox, then clicking "Delete".](/_images/image-(1974 "Checking the \"I understand the implications of deleting this app registration\" checkbox, then clicking \"Delete\".").png)

        \
        The **Welcome to Azure** page is shown and the **Delete application - Successfully deleted application PMPC Recovery** notification is shown.\
        \\

        !["App registrations" page refreshes and the "Delete application - Successfully deleted application PMPC Recovery" notification is shown.](/_images/image-(1975 "\"App registrations\" page refreshes and the \"Delete application - Successfully deleted application PMPC Recovery\" notification is shown.").png)

        \\
    6.  Click **App Registrations**.\
        \\

        ![Clicking the "App Registrations" blade](/_images/image-(1976 "Clicking the \"App Registrations\" blade").png)

        \\
    7.  On the **App registrations** screen, click **All applications**.\
        \\

        ![Clicking the "All applications" blade](/_images/image-(1977 "Clicking the \"All applications\" blade").png)

        \\
    8.  Verify the **PMPC Recovery** application has been deleted.\
        \\

        ![Verifying the "PMPC Recovery" application has been deleted.](/_images/image-(1978 "Verifying the \"PMPC Recovery\" application has been deleted.").png)