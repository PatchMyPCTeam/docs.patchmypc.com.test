---
description: Enabling user authentication using Azure Active Directory
---

# Advanced Insights Azure AD (Entra ID) Authentication

_Applies to: Patch My PC Advanced Insights_

Advanced Insights supports authentication using Entra ID credentials using OpenID. To configure this is a two-step process:

1. Create an App Registration in Entra
2. Enter the App Registration details to Advanced Insights

### Creating the App Registration <a href="#creating-the-app-registration" id="creating-the-app-registration"></a>

Navigate to the Entra Admin Centre and log in with an account that has permissions to create App Registrations.

You will add a name for the App Registration (for example _"AdvancedInsights"_).

In Supported Accounts select _<strong>"Accounts in this organizational directory only"</strong>_

<strong>Redirect URI</strong>

<blockquote class="wp-block-quote">
<p><strong>Redirect URI</strong> is used for Microsoft to return the login token to Advanced Insights.</p>
<p>\</p>
<p>This URI must be configured with the value of the internal FQDN of the server hosting Advanced Insights, including the configured port.</p>
<p>_(https://<strong>{AdvancedInsightsInternalServerFQDN}:{port}</strong>/account/login)_</p>
</blockquote>

Example redirect URI:

_https://advinsightsserver01.contoso.local:444/account/login_

Select _<strong>"Single-Page Application (SPA)"</strong>_ from the dropdown list in the <strong>"</strong>_<strong>Redirect URI"</strong>_ section, and enter the URI.

![](/_images/app-reg-(3).png "")

When you have filled in the required properties click <strong>Register</strong>.

You will be shown the App Registration overview screen. We need to copy some properties from here.

Copy <strong>Application (client) ID</strong> and <strong>Directory (tenant) ID</strong> values into a Notepad document.

![](/_images/app-reg2-(1).png "")

Now click the _"<strong>Authentication"</strong>_ link on the left in the _"<strong>Manage</strong>"_ section.

In the _"<strong>Implicit grant for hybrid flows"</strong>_ section, tick both options for:&#x20;

_<strong>"Access tokens (used for implicit flows)"</strong>_&#x20;

_<strong>"ID tokens (used for implicit and hybrid flows)"</strong>_&#x20;

This grants the application permissions to issue the tokens used by Advanced Insights to validate login.&#x20;

To save changes, click <strong>'Save'</strong>.

![](/_images/app-reg3-(1).png "")

Click "<strong>Certificates and secrets"</strong>, then within the <strong>"Client secrets"</strong> section, click _<strong>"New client secret"</strong>_.

Name the secret and set an expiry duration that is suitable for your environment.&#x20;

<blockquote class="wp-block-quote">
<p>On expiry, logins to Advanced Insights using Entra ID credentials will stop working if you don’t update the client secret.</p>
</blockquote>

![](/_images/app-reg5.png)

Click 'Add' to save the <strong>"Client secret"</strong> configuration.

Now you can copy the <strong>"Value"</strong> of your client secret and add it to your Notepad document:

![](/_images/app-reg6.png)

This completes the configuration work in the Azure Portal.

### Adding settings to Advanced Insights <a href="#adding-settings-to-callisto" id="adding-settings-to-callisto"></a>

1. Log into Advanced Insights with an <strong>administrator</strong> role account and navigate to the _<strong>'Administration' > 'Settings'</strong>_ menu. Select the _<strong>"AzureAD"</strong>_ tab.
2. Clear the _<strong>"Deactivate"</strong>_ checkbox.
3. Enter the value for your <strong>Application ID/ClientID</strong>.
4. Enter the value for your <strong>Client Secret</strong>.
5. Enter the value for your <strong>Directory (tenant) ID</strong>.
6. Select _<strong>'Save All'</strong>_.

![](/_images/advins1.png)

## <strong>New users</strong>

<blockquote class="wp-block-quote">
<p>By default, new users configured in Advanced Insights <strong>(including new Entra ID logins)</strong> will not be active (and can not login) until an administrator manually activates the account.</p>
<p>![](/_images/activation.png)</p>
</blockquote>

1. Log into Advanced Insights with an <strong>administrator</strong> role account and navigate to the _<strong>'Administration' > 'Settings'</strong>_ menu. Select the _<strong>"User Management"</strong>_ tab.
2. Enable _<strong>"New registered users are active by default."</strong>_ checkbox.
3. Select _<strong>'Save All'</strong>_.

![](/_images/newusers1.png)

This completes the configuration for adding the Entra ID App Registration details to Advanced Insights.

## <strong>First login - Consent to Permissions</strong>

The Advanced Insights logon screen will now show a _<strong>"Sign in with Microsoft"</strong>_ button.

![](/_images/advinslogin1.png)

At first logon, an Azure administrator will have to consent to the application registration requested permissions.

![](/_images/advinslogin2.png)

<blockquote class="wp-block-quote">
<p>By default, new users will only be granted access to the Advanced Insights overview home page.</p>
<p>Advanced Insights administrator can then enable access to additional dashboard views.&#x20;</p>
</blockquote>

![](/_images/home.png)

### User requirements <a href="#user-requirements" id="user-requirements"></a>

You should check in the Users area in Advanced Insights that there are no existing user accounts with email addresses that match the Entra ID accounts you are going to have logging in. If you do, you can delete these accounts and they will be recreated on first login by that user.

You will always be able to log in as the Advanced Insights "Admin" to make configuration changes.

If the Entra ID account a user logs into Advanced Insights with has a matching on-prem AD Account with the same Email Address set, any RBAC role they have in ConfigMgr for their on-prem AD account will be maintained in Advanced Insights.

For example, if a log in with this Entra ID Account is used:

![](/_images/user1.png)

The on-premises Active Directory object of this account has the users Entra ID UPN set as the email property:

![](/_images/user2.png)