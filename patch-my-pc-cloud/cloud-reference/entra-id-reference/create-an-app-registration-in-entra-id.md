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

!\[]\(/\_images/image-(542 "").png "")

2.  Click **New registration**.\
    \\

    !\[]\(/\_images/image-(543 "").png "")

    3.  In the **Name** field, enter **PMPC Recovery**, then click **Register**.\\

        !\[]\(/\_images/image-(544 "").png "")

        \\
    4.  Make a note of the following values:\
        \
        \&#xNAN;**• Application (client) ID**\
        &#xNAN;**• Object ID**\
        &#xNAN;**• Directory (tenant) ID**\\

        !\[]\(/\_images/image-(545 "").png "")

        \\
    5.  Navigate to **Manage | API Permissions**.\\

        !\[]\(/\_images/image-(546 "").png "")

        \\
    6.  Under the **Configured permissions** section, click **Add a permission**.\
        \\

        !\[]\(/\_images/image-(547 "").png "")

        \\
    7.  In the **Request API permissions** blade, click **Microsoft Graph**.\
        \\

        !\[]\(/\_images/image-(548 "").png "")

        \\
    8.  In the **Request API permissions** blade, click **Application permissions**.\
        \\

        !\[]\(/\_images/image-(549 "").png "")

        \\
    9.  In the **Select permissions** field, type **AuditLog**, then expand this section and check the **AuditLog.Read.All** permission checkbox.\\

        !\[]\(/\_images/image-(550 "").png "")

        \\
    10. Click **Add permissions**.\
        \\

        !\[]\(/\_images/image-(551 "").png "")

        \\
    11. On the **API permissions** screen, under the **Configured permissions** section, click **Grant admin consent for <**_**your\_tenant\_name**_**>**.\\

        !\[]\(/\_images/image-(552 "").png "")”">

        \\
    12. On the **Grant admin consent confirmation** popup, click **Yes**.\
        \\

        !\[]\(/\_images/image-(553 "").png "")

        The **Grant consent - Grant consent successful** notification is shown and the **Status** for the **AuditLog.Read.All** permission changes to a green tick.\\

        !\[]\(/\_images/image-(554 "").png "")

        \\
    13. Navigate to **Certificates and secrets**.\
        \\

        !\[]\(/\_images/image-(555 "").png "")

        \\
    14. Under the **Client secrets** section, click **New client secret**.\
        \\

        !\[]\(/\_images/image-(556 "").png "")

        \\
    15. In the **Add a client secret** panel, type **PMPC Recovery**, then click **Add**.\
        \\

        !\[]\(/\_images/image-(557 "").png "")

        \
        The new Client Secret appears along with the **Update application credentials - Successfully updated application PMPC Recovery credentials** notification.\
        \\

        !\[]\(/\_images/image-(558 "").png "")
    16. Make a note of the **Value** of the **PMPC Recovery** client secret.
