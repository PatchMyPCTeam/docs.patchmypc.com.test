# Permissions required for Patch My PC Cloud

_Applies to: Patch My PC Cloud_

To onboard to Patch My PC (PMPC) Cloud, we require the following permissions:

| Permission                                          | Claim           | Description                                                                                                                                                                                                                                                                          |
| --------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| View your basic profile                             | profile         | <p>Allows the app to see your basic profile (e.g., name, picture, user name, email address).</p><p>This is a permission requested to access your data in your Intune Tenant.</p>                                                                                                     |
| Maintain access to data you have given it access to | offline\_access | <p>Allows the app to see and update the data you gave it access to, even when you are not currently using the app. This does not give the app any additional permissions.</p><p>This is a permission requested to access your data in &#x3C;<em>your_intune_tenant's_name</em>>.</p> |

As per the dialog box:

“_Accepting these permissions means that you allow this app to use your data as specified in their_ [_terms of service_](https://patchmypc.com/terms-of-service) _and_ [_privacy statement_](https://patchmypc.com/privacy-policy)_. You can change these permissions at_ [_https://myapps.microsoft.com_](https://myapps.microsoft.com)_._ [_Show details_](https://login.microsoftonline.com/common/login)_._”

You will be prompted to grant these during the onboarding process by clicking **Accept** on the **Permissions requested** dialog box.

![](/_images/image-(1351 "").png "")

{% hint style="info" %}
**Note**

Whether or not you see the **Permissions Required** dialog box and what you see on it depends on the account you use to sign into Entra and how the **User consent for applications** settings are configured in your environment.

![“User consent settings for applications” Entra settings.](<../../../.gitbook/assets/image (962).png>)

You will only see the C**onsent on behalf of your organization** checkbox if the user account you are signed in with is a Global Admin.

How the **User consent for applications** settings are configured determines whether you can sign up for the PMPC Cloud or not.

If **Do not allow user consent** is configured, you will not see the **Permissions Requested** dialog box, but an error prompting you to contact an administrator.

If either **Allow user consent for apps from verified publishers, for selected permissions (Recommended)** or **Allow user consent for apps** is configured, any user can register for the PMPC Cloud and complete the app registration.

Also, if you will use the Intune Apps Feature, the onboarding process requires additional permissions as detailed in [Permissions required for Intune Apps](permissions-required-for-intune-apps.md).
{% endhint %}
