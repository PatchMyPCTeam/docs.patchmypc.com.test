# Create an App Registration in Entra ID

_Applies to: Patch My PC Cloud_

There may be some scenarios (such as [Recover Your Company](../../cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) ) where you need to create an App Registration in Entra ID for use with Patch My PC (PMPC) Cloud.

{% hint style="warning" %}
**Important**

Once you create an App Registration, it must be used within 72 hours; otherwise, it will be considered expired, and you will need to create a new one.
{% endhint %}

We use this process to verify you are an Application Administrator or a higher privilege user (such as a Global Admin), in the same Entra ID tenant as the PMPC Company being managed.

To create an App Registration:

1. Sign in to the Microsoft Azure portal using an account with the Global Admin role and navigate to the [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) blade.

{% hint style="warning" %}
**Important**

You must use an account in the same Microsoft 365 subscription (tenant) as your PMPC Company.
{% endhint %}

![Navigating to the “App registrations” blade](/_images/image%20%28542%29.png "Navigating to the \"App registrations\" blade")

2.  Click **New registration**.\
    \


    ![Clicking “New registration”](/_images/image%20%28543%29.png "Clicking \"New registration\"")



    3.  In the **Name** field, enter **PMPC Recovery**, then click **Register**.\


        ![Entering “PMPC Recovery” then clicking “Register”](/_images/image%20%28544%29.png "Entering \"PMPC Recovery\" then clicking \"Register\"")

        \

    4.  Make a note of the following values:\
        \
        &#xNAN;**• Application (client) ID**\
        **• Object ID**\
        **• Directory (tenant) ID**\


        ![Noting the required values](/_images/image%20%28545%29.png "Noting the required values")

        \

    5.  Navigate to **Manage | API Permissions**.\


        ![Navigating to “Manage | API Permissions”](/_images/image%20%28546%29.png "Navigating to \"Manage | API Permissions\"")

        \

    6.  Under the **Configured permissions** section, click **Add a permission**.\
        \


        ![Clicking “Add a permission”](/_images/image%20%28547%29.png "Clicking \"Add a permission\"")

        \

    7.  In the **Request API permissions** blade, click **Microsoft Graph**.\
        \


        ![Clicking “Microsoft Graph”](/_images/image%20%28548%29.png "Clicking \"Microsoft Graph\"")

        \

    8.  In the **Request API permissions** blade, click **Application permissions**.\
        \


        ![Clicking “Application permissions”](/_images/image%20%28549%29.png "Clicking \"Application permissions\"")

        \

    9.  In the **Select permissions** field, type **AuditLog**, then expand this section and check the **AuditLog.Read.All** permission checkbox.\


        ![Checking the “AuditLog.Read.All” permission checkbox](/_images/image%20%28550%29.png "Checking the \"AuditLog.Read.All\" permission checkbox")

        \

    10. Click **Add permissions**.\
        \


        ![Clicking “Add permissions”](/_images/image%20%28551%29.png "Clicking \"Add permissions\"")

        \

    11. On the **API permissions** screen, under the **Configured permissions** section, click **Grant admin consent for <**_**your\_tenant\_name**_**>**.\


        ![](/_images/image%20%28552%29.png "")

        \

    12. On the **Grant admin consent confirmation** popup, click **Yes**.\
        \


        ![Clicking “Yes” on the “Grant admin consent confirmation” popup](/_images/image%20%28553%29.png "Clicking \"Yes\" on the \"Grant admin consent confirmation\" popup")

        The **Grant consent - Grant consent successful** notification is shown and the **Status** for the **AuditLog.Read.All** permission changes to a green tick.\


        ![“Grant consent - Grant consent successful notification” shown and the “Status” for the “AuditLog.Read.All” permission changes to a green tick.](/_images/image%20%28554%29.png "\"Grant consent - Grant consent successful notification\" shown and the \"Status\" for the \"AuditLog.Read.All\" permission changes to a green tick.")

        \

    13. Navigate to **Certificates and secrets**.\
        \


        ![Navigating to “Certificates and secrets”](/_images/image%20%28555%29.png "Navigating to \"Certificates and secrets\"")

        \

    14. Under the **Client secrets** section, click **New client secret**.\
        \


        ![Clicking “New client secret” under the “Client secrets” section](/_images/image%20%28556%29.png "Clicking \"New client secret\" under the \"Client secrets\" section")

        \

    15. In the **Add a client secret** panel, type **PMPC Recovery**, then click **Add**.\
        \


        ![Typing “PMPC Recovery” in the “Description” field, then clicking “Add”](/_images/image%20%28557%29.png "Typing \"PMPC Recovery\" in the \"Description\" field, then clicking \"Add\"")

        \
        The new Client Secret appears along with the **Update application credentials - Successfully updated application PMPC Recovery credentials** notification.\
        \


        ![New Client Secret and the “Update application credentials - Successfully updated application PMPC Recovery credentials” notification](/_images/image%20%28558%29.png "New Client Secret and the \"Update application credentials - Successfully updated application PMPC Recovery credentials\" notification")


    16. Make a note of the **Value** of the **PMPC Recovery** client secret.
