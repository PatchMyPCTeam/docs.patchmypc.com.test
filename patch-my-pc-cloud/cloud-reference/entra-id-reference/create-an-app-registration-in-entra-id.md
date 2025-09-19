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

![Navigating to the “App registrations” blade](<../../../.gitbook/assets/image-(542) (1).png>)

2.  Click **New registration**.\
    \\

    ![Clicking “New registration”](<../../../.gitbook/assets/image-(543) (1).png>)

    3.  In the **Name** field, enter **PMPC Recovery**, then click **Register**.\\

        ![Entering “PMPC Recovery” then clicking “Register”](<../../../.gitbook/assets/image-(544) (1).png>)

        \\
    4.  Make a note of the following values:\
        \
        \&#xNAN;**• Application (client) ID**\
        &#xNAN;**• Object ID**\
        &#xNAN;**• Directory (tenant) ID**\\

        ![Noting the required values](<../../../.gitbook/assets/image-(545) (1).png>)

        \\
    5.  Navigate to **Manage | API Permissions**.\\

        ![Navigating to “Manage | API Permissions”](<../../../.gitbook/assets/image-(546) (1).png>)

        \\
    6.  Under the **Configured permissions** section, click **Add a permission**.\
        \\

        ![Clicking “Add a permission”](<../../../.gitbook/assets/image-(547) (1).png>)

        \\
    7.  In the **Request API permissions** blade, click **Microsoft Graph**.\
        \\

        ![Clicking “Microsoft Graph”](<../../../.gitbook/assets/image-(548) (1).png>)

        \\
    8.  In the **Request API permissions** blade, click **Application permissions**.\
        \\

        ![Clicking “Application permissions”](<../../../.gitbook/assets/image-(549) (1).png>)

        \\
    9.  In the **Select permissions** field, type **AuditLog**, then expand this section and check the **AuditLog.Read.All** permission checkbox.\\

        ![Checking the “AuditLog.Read.All” permission checkbox](<../../../.gitbook/assets/image-(550) (1).png>)

        \\
    10. Click **Add permissions**.\
        \\

        ![Clicking “Add permissions”](<../../../.gitbook/assets/image-(551) (1).png>)

        \\
    11. On the **API permissions** screen, under the **Configured permissions** section, click **Grant admin consent for <**_**your\_tenant\_name**_**>**.\\

        ![](../../../.gitbook/assets/image-\(552\).png)

        \\
    12. On the **Grant admin consent confirmation** popup, click **Yes**.\
        \\

        ![Clicking “Yes” on the “Grant admin consent confirmation” popup](<../../../.gitbook/assets/image-(553) (1).png>)

        The **Grant consent - Grant consent successful** notification is shown and the **Status** for the **AuditLog.Read.All** permission changes to a green tick.\\

        ![“Grant consent - Grant consent successful notification” shown and the “Status” for the “AuditLog.Read.All” permission changes to a green tick.](<../../../.gitbook/assets/image-(554) (1).png>)

        \\
    13. Navigate to **Certificates and secrets**.\
        \\

        ![Navigating to “Certificates and secrets”](<../../../.gitbook/assets/image-(555) (1).png>)

        \\
    14. Under the **Client secrets** section, click **New client secret**.\
        \\

        ![Clicking “New client secret” under the “Client secrets” section](<../../../.gitbook/assets/image-(556) (1).png>)

        \\
    15. In the **Add a client secret** panel, type **PMPC Recovery**, then click **Add**.\
        \\

        ![Typing “PMPC Recovery” in the “Description” field, then clicking “Add”](<../../../.gitbook/assets/image-(557) (1).png>)

        \
        The new Client Secret appears along with the **Update application credentials - Successfully updated application PMPC Recovery credentials** notification.\
        \\

        ![New Client Secret and the “Update application credentials - Successfully updated application PMPC Recovery credentials” notification](<../../../.gitbook/assets/image-(558) (1).png>)
    16. Make a note of the **Value** of the **PMPC Recovery** client secret.
