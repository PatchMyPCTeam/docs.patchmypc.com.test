# Create an App Registration in Entra ID

_Applies to: Patch My PC Cloud_

There may be some scenarios (such as [Recover Your Company](../../cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) ) where you need to create an App Registration in Entra ID for use with Patch My PC (PMPC) Cloud.

> **Important**
>
> Once you create an App Registration, it must be used within 72 hours; otherwise, it will be considered expired, and you will need to create a new one.

We use this process to verify you are an Application Administrator or a higher privilege user (such as a Global Admin), in the same Entra ID tenant as the PMPC Company being managed.

To create an App Registration:

1. Sign in to the Microsoft Azure portal using an account with the Global Admin role and navigate to the [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) blade.

> **Important**
>
> You must use an account in the same Microsoft 365 subscription (tenant) as your PMPC Company.

![Navigating to the "App registrations" blade](/_images/image-(542 "Navigating to the \"App registrations\" blade").png)

2.  Click **New registration**.\
    \\

    ![Clicking "New registration"](/_images/image-(543 "Clicking \"New registration\"").png)

    3.  In the **Name** field, enter **PMPC Recovery**, then click **Register**.\\

        ![Entering "PMPC Recovery" then clicking "Register"](/_images/image-(544 "Entering \"PMPC Recovery\" then clicking \"Register\"").png)

        \\
    4.  Make a note of the following values:\
        \
        \&#xNAN;**• Application (client) ID**\
        &#xNAN;**• Object ID**\
        &#xNAN;**• Directory (tenant) ID**\\

        ![Noting the required values](/_images/image-(545 "Noting the required values").png)

        \\
    5.  Navigate to **Manage | API Permissions**.\\

        ![Navigating to "Manage | API Permissions"](/_images/image-(546 "Navigating to \"Manage | API Permissions\"").png)

        \\
    6.  Under the **Configured permissions** section, click **Add a permission**.\
        \\

        ![Clicking "Add a permission"](/_images/image-(547 "Clicking \"Add a permission\"").png)

        \\
    7.  In the **Request API permissions** blade, click **Microsoft Graph**.\
        \\

        ![Clicking "Microsoft Graph"](/_images/image-(548 "Clicking \"Microsoft Graph\"").png)

        \\
    8.  In the **Request API permissions** blade, click **Application permissions**.\
        \\

        ![Clicking "Application permissions"](/_images/image-(549 "Clicking \"Application permissions\"").png)

        \\
    9.  In the **Select permissions** field, type **AuditLog**, then expand this section and check the **AuditLog.Read.All** permission checkbox.\\

        ![Checking the "AuditLog.Read.All" permission checkbox](/_images/image-(550 "Checking the \"AuditLog.Read.All\" permission checkbox").png)

        \\
    10. Click **Add permissions**.\
        \\

        ![Clicking "Add permissions"](/_images/image-(551 "Clicking \"Add permissions\"").png)

        \\
    11. On the **API permissions** screen, under the **Configured permissions** section, click **Grant admin consent for <**_**your\_tenant\_name**_**>**.\\

        ![](/_images/image-(552).png)

        \\
    12. On the **Grant admin consent confirmation** popup, click **Yes**.\
        \\

        ![Clicking "Yes" on the "Grant admin consent confirmation" popup](/_images/image-(553 "Clicking \"Yes\" on the \"Grant admin consent confirmation\" popup").png)

        The **Grant consent - Grant consent successful** notification is shown and the **Status** for the **AuditLog.Read.All** permission changes to a green tick.\\

        !["Grant consent - Grant consent successful notification" shown and the "Status" for the "AuditLog.Read.All" permission changes to a green tick.](/_images/image-(554 "\"Grant consent - Grant consent successful notification\" shown and the \"Status\" for the \"AuditLog.Read.All\" permission changes to a green tick.").png)

        \\
    13. Navigate to **Certificates and secrets**.\
        \\

        ![Navigating to "Certificates and secrets"](/_images/image-(555 "Navigating to \"Certificates and secrets\"").png)

        \\
    14. Under the **Client secrets** section, click **New client secret**.\
        \\

        ![Clicking "New client secret" under the "Client secrets" section](/_images/image-(556 "Clicking \"New client secret\" under the \"Client secrets\" section").png)

        \\
    15. In the **Add a client secret** panel, type **PMPC Recovery**, then click **Add**.\
        \\

        ![Typing "PMPC Recovery" in the "Description" field, then clicking "Add"](/_images/image-(557 "Typing \"PMPC Recovery\" in the \"Description\" field, then clicking \"Add\"").png)

        \
        The new Client Secret appears along with the **Update application credentials - Successfully updated application PMPC Recovery credentials** notification.\
        \\

        ![New Client Secret and the "Update application credentials - Successfully updated application PMPC Recovery credentials" notification](/_images/image-(558 "New Client Secret and the \"Update application credentials - Successfully updated application PMPC Recovery credentials\" notification").png)
    16. Make a note of the **Value** of the **PMPC Recovery** client secret.