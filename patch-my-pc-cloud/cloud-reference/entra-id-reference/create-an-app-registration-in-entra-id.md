# Create an App Registration in Entra ID

_Applies to: Patch My PC Cloud_

There may be some scenarios (such as [Recover Your Company](../../cloud-administration/manage-your-cloud-company/recover-your-cloud-company.md) ) where you need to create an App Registration in Entra ID for use with Patch My PC (PMPC) Cloud.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>Once you create an App Registration, it must be used within 72 hours; otherwise, it will be considered expired, and you will need to create a new one.</p>
</blockquote>

We use this process to verify you are an Application Administrator or a higher privilege user (such as a Global Admin), in the same Entra ID tenant as the PMPC Company being managed.

To create an App Registration:

1. Sign in to the Microsoft Azure portal using an account with the Global Admin role and navigate to the [App Registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) blade.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>You must use an account in the same Microsoft 365 subscription (tenant) as your PMPC Company.</p>
</blockquote>

![Navigating to the “App registrations” blade](/_images/image-(542).png "Navigating to the “App registrations” blade")

2.  Click <strong>New registration</strong>.\
    \


    ![Clicking “New registration”](/_images/image-(543).png "Clicking “New registration”")



    3.  In the <strong>Name</strong> field, enter <strong>PMPC Recovery</strong>, then click <strong>Register</strong>.\


        ![Entering “PMPC Recovery” then clicking “Register”](/_images/image-(544).png "Entering “PMPC Recovery” then clicking “Register”")

        \

    4.  Make a note of the following values:\
        \
        &#xNAN;<strong>• Application (client) ID</strong>\
        <strong>• Object ID</strong>\
        <strong>• Directory (tenant) ID</strong>\


        ![Noting the required values](/_images/image-(545).png "Noting the required values")

        \

    5.  Navigate to <strong>Manage | API Permissions</strong>.\


        ![Navigating to “Manage | API Permissions”](/_images/image-(546).png "Navigating to “Manage | API Permissions”")

        \

    6.  Under the <strong>Configured permissions</strong> section, click <strong>Add a permission</strong>.\
        \


        ![Clicking “Add a permission”](/_images/image-(547).png "Clicking “Add a permission”")

        \

    7.  In the <strong>Request API permissions</strong> blade, click <strong>Microsoft Graph</strong>.\
        \


        ![Clicking “Microsoft Graph”](/_images/image-(548).png "Clicking “Microsoft Graph”")

        \

    8.  In the <strong>Request API permissions</strong> blade, click <strong>Application permissions</strong>.\
        \


        ![Clicking “Application permissions”](/_images/image-(549).png "Clicking “Application permissions”")

        \

    9.  In the <strong>Select permissions</strong> field, type <strong>AuditLog</strong>, then expand this section and check the <strong>AuditLog.Read.All</strong> permission checkbox.\


        ![Checking the “AuditLog.Read.All” permission checkbox](/_images/image-(550).png "Checking the “AuditLog.Read.All” permission checkbox")

        \

    10. Click <strong>Add permissions</strong>.\
        \


        ![Clicking “Add permissions”](/_images/image-(551).png "Clicking “Add permissions”")

        \

    11. On the <strong>API permissions</strong> screen, under the <strong>Configured permissions</strong> section, click <strong>Grant admin consent for <</strong>_<strong>your\_tenant\_name</strong>_<strong>></strong>.\


        ![](/_images/image-(552).png "")

        \

    12. On the <strong>Grant admin consent confirmation</strong> popup, click <strong>Yes</strong>.\
        \


        ![Clicking “Yes” on the “Grant admin consent confirmation” popup](/_images/image-(553).png "Clicking “Yes” on the “Grant admin consent confirmation” popup")

        The <strong>Grant consent - Grant consent successful</strong> notification is shown and the <strong>Status</strong> for the <strong>AuditLog.Read.All</strong> permission changes to a green tick.\


        ![“Grant consent - Grant consent successful notification” shown and the “Status” for the “AuditLog.Read.All” permission changes to a green tick.](/_images/image-(554).png "“Grant consent - Grant consent successful notification” shown and the “Status” for the “AuditLog.Read.All” permission changes to a green tick.")

        \

    13. Navigate to <strong>Certificates and secrets</strong>.\
        \


        ![Navigating to “Certificates and secrets”](/_images/image-(555).png "Navigating to “Certificates and secrets”")

        \

    14. Under the <strong>Client secrets</strong> section, click <strong>New client secret</strong>.\
        \


        ![Clicking “New client secret” under the “Client secrets” section](/_images/image-(556).png "Clicking “New client secret” under the “Client secrets” section")

        \

    15. In the <strong>Add a client secret</strong> panel, type <strong>PMPC Recovery</strong>, then click <strong>Add</strong>.\
        \


        ![Typing “PMPC Recovery” in the “Description” field, then clicking “Add”](/_images/image-(557).png "Typing “PMPC Recovery” in the “Description” field, then clicking “Add”")

        \
        The new Client Secret appears along with the <strong>Update application credentials - Successfully updated application PMPC Recovery credentials</strong> notification.\
        \


        ![New Client Secret and the “Update application credentials - Successfully updated application PMPC Recovery credentials” notification](/_images/image-(558).png "New Client Secret and the “Update application credentials - Successfully updated application PMPC Recovery credentials” notification")


    16. Make a note of the <strong>Value</strong> of the <strong>PMPC Recovery</strong> client secret.