# Recover your Cloud Company

_Applies to: Patch My PC Cloud_

To prevent access issues to your Patch My PC (PMPC) Cloud company, we highly recommend granting at least two users the [Full Admin with Access Management](../manage-cloud-users/cloud-user-roles-reference.md) user role

{% hint style="info" %}
**Note**

If you only have one user assigned the Full Admin with Access Management role, the [You currently have only one user with Access Management privileges](../../cloud-troubleshooting/troubleshooting-cloud-users/you-currently-have-only-one-user-with-access-management-privileges-error-in-cloud.md) banner is displayed.
{% endhint %}

However, if you have not done this and the only user with this role leaves your company, you will no longer be able to manage both existing and new users within your PMPC Company.

Your only option is to attempt to recover your company, which involves providing us with specific details from the same Entra ID tenant as your PMPC Company to confirm your identity and validate your request. If successful, the user account performing the recovery will be granted the Full Admin with Access Management role.

{% hint style="info" %}
**Note**

See the [Creating an App Registration in Entra ID](../../cloud-reference/entra-id-reference/create-an-app-registration-in-entra-id.md) process for details on how to create and obtain these values.
{% endhint %}

{% hint style="warning" %}
**Important**

We provide the functionality to disable a PMPC company from being recovered. However, we do not display and enable this by default because if it's enabled and you lose access to your company for whatever reason, neither of us can regain access to that company. This means you'll lose everything and need to create a new company and reconfigure it to match the old one. If you really want to enable this feature, please \
[open a support case](https://patchmypc.com/technical-support).
{% endhint %}

### Requirements

The user performing the recovery process does not need to be an existing user in the PMPC Company being recovered.

However, to verify the ID of the user performing the recovery, we ask them to create various objects in the same Entra ID tenant as the PMPC Company being retrieved. Once created, the values of these new objects and other existing objects need to be entered into our **Claim Ownership** wizard.

To create and retrieve the values of the required objects, the user performing the recovery process has to be an **Application Administrator** or a higher privilege user (such as a **Global Admin**), in the same Entra ID tenant as the PMPC Company being recovered.&#x20;

Alternatively, they can request a user with these privileges complete the Entra ID processes and provide the required values to the user performing the recovery so that they can complete the **Claim Ownership** wizard.

### Recovering a Company

To recover a PMPC Company:

1. If the user attempting the recovery is an existing user and is already logged in, they must sign out of any portal sessions for that company.
2.  Navigate to [https://portal.patchmypc.com/](https://portal.patchmypc.com/)\


    <figure><img src="/_images/gitbook/image%20%28488%29.png" alt="" width="563"><figcaption></figcaption></figure>
3. Click **Sign In** if the user attempting the recovery can sign in to multiple companies in PMPC Cloud.
4.  Click **Sign Up** if any of the following applies to the user attempting recovery:\


    a) The user only belongs to a single company i.e. the account is not used to manage multiple companies in PMPC Cloud.\
    \
    b) The user has not signed into the portal before and is not associated with an existing PMPC Cloud company.
5.  On the **Select the Company You Want to Sign In To** screen, click **Recover Company**.\


    <figure><img src="/_images/gitbook/image%20%281955%29.png" alt="Clicking “Recover Company”" width="563"><figcaption></figcaption></figure>

    \
    The **Claim Ownership** wizard starts.\


    <figure><img src="/_images/gitbook/image%20%282190%29.png" alt="“Claim Ownership” wizard" width="563"><figcaption></figcaption></figure>


6.  From the **Company to Claim** dropdown, select the company you want to recover.\


    <figure><img src="/_images/gitbook/image%20%282191%29.png" alt="“Company to Claim” dropdown" width="563"><figcaption></figcaption></figure>

    \
    The last five characters of the **Directory (tenant) ID** of the Entra ID to which your PMPC Company belongs are shown.\


    <figure><img src="/_images/gitbook/image%20%282192%29.png" alt="Last five characters of the Directory (tenant) ID of the Entra ID to which your PMPC Company belongs are shown." width="563"><figcaption></figcaption></figure>


7. Using the [Creating an App Registration in Entra ID](../../cloud-reference/entra-id-reference/create-an-app-registration-in-entra-id.md) process, verify that the last five characters of the Entra ID match the last five characters of the **Directory (tenant) ID**.\
   \
   If they match, continue.\
   \
   If they don’t match, you are looking in the wrong Entra ID tenant and the ownership process will fail with the [Error - Claim Ownership Failed.](../../cloud-troubleshooting/troubleshooting-a-cloud-company/error-claim-ownership-failed-when-trying-to-recover-a-cloud-company.md)
8.  Continue following the [Creating an App Registration in Entra ID](../../cloud-reference/entra-id-reference/create-an-app-registration-in-entra-id.md) process to create the relevant App Registration in your Entra ID tenant.\
    \
    From this process, you are going to need the following values:\


    • Object ID\
    • Application (client) ID for the PMPC Recovery App Registration\
    • PMPC Recovery client secret.
9. Copy the following values from the [Creating an App Registration in Entra ID](../../cloud-reference/entra-id-reference/create-an-app-registration-in-entra-id.md) process to their respective fields of the **Claim Ownership** wizard:

{% hint style="warning" %}
**Important**

You cannot use an App Registration older than 72 hours to perform the recovery of a company.
{% endhint %}

| Entra ID Value                                                 | Claim Ownership field |
| -------------------------------------------------------------- | --------------------- |
| Object ID                                                      | Object ID             |
| Application (client) ID for the PMPC Recovery App Registration | Client ID             |
| PMPC Recovery client secret.                                   | Secret                |

<figure><img src="/_images/gitbook/image%20%282195%29.png" alt="Completed “Claim Ownership” wizard" width="563"><figcaption></figcaption></figure>

10. Click **Continue**.\


    <figure><img src="/_images/gitbook/image%20%282194%29.png" alt="Clicking &#x22;Continue&#x22;" width="563"><figcaption></figcaption></figure>
11. If the user performing the recovery is an existing user within the PMPC Company, go to Step 15.
12. If the user performing the recovery is not an existing user within the PMPC Company, they will see the **User Info** page.\


    <figure><img src="/_images/gitbook/image%20%281962%29.png" alt="“User Info” page" width="563"><figcaption></figcaption></figure>


13. Complete the **First Name** and **Last Name** fields, which will be used to create the new account and assign them the **Full Admin with Access Management** role if the recovery is successful.
14. Review the **Terms and conditions** and if you are happy, click to check the **Accept all Terms and conditions** checkbox, then click **Continue**.\


    <figure><img src="/_images/gitbook/image%20%281963%29.png" alt="Checking the “Accept all Terms and conditions” checkbox, then clicking “Continue”." width="563"><figcaption></figcaption></figure>


15. The supplied information is checked.\
    \
    If the recovery process fails, see the **Resolution** section of the [Error – Claim Ownership Failed](../../cloud-troubleshooting/troubleshooting-a-cloud-company/error-claim-ownership-failed-when-trying-to-recover-a-cloud-company.md) article for troubleshooting help.\
    \
    If the recovery process is successful, the **Ownership Granted** popup is displayed.\


    <figure><img src="/_images/gitbook/image%20%281965%29.png" alt="“Ownership Granted” popup" width="503"><figcaption></figcaption></figure>



{% hint style="danger" %}
**Important**&#x20;

You have three attempts to recover a company. If recovery fails after the third attempt, you will need to wait 12 hours before you can attempt recovery again.
{% endhint %}

16. Click **Close** to complete the recovery process and display the **App Catalog** page of the recovered company.\


    <figure><img src="/_images/gitbook/image%20%281966%29.png" alt="“App Catalog” page of the recovered company " width="563"><figcaption></figcaption></figure>

    \
    If you navigate to the **Users** node, you will see that the account used to perform the recovery process has been created (if applicable) and assigned the **Full Admin with Access Management** role.\


    <figure><img src="/_images/gitbook/image%20%281967%29.png" alt="“Users” node showing the user account used to perform the recovery process has been created (if applicable) and assigned the “Full Admin with Access Management role”." width="563"><figcaption></figcaption></figure>

    \
    If you navigate to the **Events** node, you will see that the **Company Ownership Approved for <**_**user\_name**_**>** event confirming the name of the user who performed the recovery process.\


    <figure><img src="/_images/gitbook/image%20%281968%29.png" alt="“Events” node showing the “Company Ownership Approved for <user_name>” event confirming the name of the user who performed the recovery process. " width="563"><figcaption></figcaption></figure>

    \
    The previous owner will also receive an email with the subject **Access Recovered to “PMPC\_<**_**company\_name**_**>”**, containing details of who performed the recovery and when.

{% hint style="info" %}
**Note**

See [Example Account Recovery Email](../../cloud-reference/cloud-email-reference/example-cloud-account-recovery-email.md) for more details and an example of the email.
{% endhint %}

{% hint style="warning" %}
**Important**

Once you have successfully completed the recovery process, to avoid potential security issues and prevent unwanted re-use of these objects, you should follow the [Deleting an App Registration in Entra ID](../../cloud-reference/entra-id-reference/delete-an-app-registration-in-entra-id.md) process to delete the recovery objects created in your Entra ID.
{% endhint %}
