# Recover your Cloud Company

_Applies to: Patch My PC Cloud_

To prevent access issues to your Patch My PC (PMPC) Cloud company, we highly recommend granting at least two users the [Full Admin with Access Management](../manage-cloud-users/cloud-user-roles-reference.md) user role

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If you only have one user assigned the Full Admin with Access Management role, the [You currently have only one user with Access Management privileges](../../cloud-troubleshooting/troubleshooting-cloud-users/you-currently-have-only-one-user-with-access-management-privileges-error-in-cloud.md) banner is displayed.</p>
</blockquote>

However, if you have not done this and the only user with this role leaves your company, you will no longer be able to manage both existing and new users within your PMPC Company.

Your only option is to attempt to recover your company, which involves providing us with specific details from the same Entra ID tenant as your PMPC Company to confirm your identity and validate your request. If successful, the user account performing the recovery will be granted the Full Admin with Access Management role.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See the [Creating an App Registration in Entra ID](../../cloud-reference/entra-id-reference/create-an-app-registration-in-entra-id.md) process for details on how to create and obtain these values.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>We provide the functionality to disable a PMPC company from being recovered. However, we do not display and enable this by default because if it's enabled and you lose access to your company for whatever reason, neither of us can regain access to that company. This means you'll lose everything and need to create a new company and reconfigure it to match the old one. If you really want to enable this feature, please \</p>
<p><a href="https://patchmypc.com/technical-support">open a support case</a>.</p>
</blockquote>

### Requirements

The user performing the recovery process does not need to be an existing user in the PMPC Company being recovered.

However, to verify the ID of the user performing the recovery, we ask them to create various objects in the same Entra ID tenant as the PMPC Company being retrieved. Once created, the values of these new objects and other existing objects need to be entered into our <strong>Claim Ownership</strong> wizard.

To create and retrieve the values of the required objects, the user performing the recovery process has to be an <strong>Application Administrator</strong> or a higher privilege user (such as a <strong>Global Admin</strong>), in the same Entra ID tenant as the PMPC Company being recovered.&#x20;

Alternatively, they can request a user with these privileges complete the Entra ID processes and provide the required values to the user performing the recovery so that they can complete the <strong>Claim Ownership</strong> wizard.

### Recovering a Company

To recover a PMPC Company:

1. If the user attempting the recovery is an existing user and is already logged in, they must sign out of any portal sessions for that company.
2.  Navigate to [https://portal.patchmypc.com/](https://portal.patchmypc.com/)\


    ![](/_images/image-(488).png "")
3. Click <strong>Sign In</strong> if the user attempting the recovery can sign in to multiple companies in PMPC Cloud.
4.  Click <strong>Sign Up</strong> if any of the following applies to the user attempting recovery:\


    a) The user only belongs to a single company i.e. the account is not used to manage multiple companies in PMPC Cloud.\
    \
    b) The user has not signed into the portal before and is not associated with an existing PMPC Cloud company.
5.  On the <strong>Select the Company You Want to Sign In To</strong> screen, click <strong>Recover Company</strong>.\


    ![Clicking “Recover Company”](/_images/image-(1955).png "Clicking “Recover Company”")

    \
    The <strong>Claim Ownership</strong> wizard starts.\


    ![“Claim Ownership” wizard](/_images/image-(2190).png "“Claim Ownership” wizard")


6.  From the <strong>Company to Claim</strong> dropdown, select the company you want to recover.\


    ![“Company to Claim” dropdown](/_images/image-(2191).png "“Company to Claim” dropdown")

    \
    The last five characters of the <strong>Directory (tenant) ID</strong> of the Entra ID to which your PMPC Company belongs are shown.\


    ![Last five characters of the Directory (tenant) ID of the Entra ID to which your PMPC Company belongs are shown.](/_images/image-(2192).png "Last five characters of the Directory (tenant) ID of the Entra ID to which your PMPC Company belongs are shown.")


7. Using the [Creating an App Registration in Entra ID](../../cloud-reference/entra-id-reference/create-an-app-registration-in-entra-id.md) process, verify that the last five characters of the Entra ID match the last five characters of the <strong>Directory (tenant) ID</strong>.\
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
9. Copy the following values from the [Creating an App Registration in Entra ID](../../cloud-reference/entra-id-reference/create-an-app-registration-in-entra-id.md) process to their respective fields of the <strong>Claim Ownership</strong> wizard:

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>You cannot use an App Registration older than 72 hours to perform the recovery of a company.</p>
</blockquote>

| Entra ID Value                                                 | Claim Ownership field |
| -------------------------------------------------------------- | --------------------- |
| Object ID                                                      | Object ID             |
| Application (client) ID for the PMPC Recovery App Registration | Client ID             |
| PMPC Recovery client secret.                                   | Secret                |

![Completed “Claim Ownership” wizard](/_images/image-(2195).png "Completed “Claim Ownership” wizard")

10. Click <strong>Continue</strong>.\


    ![Clicking &#x22;Continue&#x22;](/_images/image-(2194).png "Clicking &#x22;Continue&#x22;")
11. If the user performing the recovery is an existing user within the PMPC Company, go to Step 15.
12. If the user performing the recovery is not an existing user within the PMPC Company, they will see the <strong>User Info</strong> page.\


    ![“User Info” page](/_images/image-(1962).png "“User Info” page")


13. Complete the <strong>First Name</strong> and <strong>Last Name</strong> fields, which will be used to create the new account and assign them the <strong>Full Admin with Access Management</strong> role if the recovery is successful.
14. Review the <strong>Terms and conditions</strong> and if you are happy, click to check the <strong>Accept all Terms and conditions</strong> checkbox, then click <strong>Continue</strong>.\


    ![Checking the “Accept all Terms and conditions” checkbox, then clicking “Continue”.](/_images/image-(1963).png "Checking the “Accept all Terms and conditions” checkbox, then clicking “Continue”.")


15. The supplied information is checked.\
    \
    If the recovery process fails, see the <strong>Resolution</strong> section of the [Error – Claim Ownership Failed](../../cloud-troubleshooting/troubleshooting-a-cloud-company/error-claim-ownership-failed-when-trying-to-recover-a-cloud-company.md) article for troubleshooting help.\
    \
    If the recovery process is successful, the <strong>Ownership Granted</strong> popup is displayed.\


    ![“Ownership Granted” popup](/_images/image-(1965).png "“Ownership Granted” popup")



<blockquote class="wp-block-quote">
<p><strong>Important</strong>&#x20;</p>
<p>You have three attempts to recover a company. If recovery fails after the third attempt, you will need to wait 12 hours before you can attempt recovery again.</p>
</blockquote>

16. Click <strong>Close</strong> to complete the recovery process and display the <strong>App Catalog</strong> page of the recovered company.\


    ![“App Catalog” page of the recovered company](/_images/image-(1966).png "“App Catalog” page of the recovered company")

    \
    If you navigate to the <strong>Users</strong> node, you will see that the account used to perform the recovery process has been created (if applicable) and assigned the <strong>Full Admin with Access Management</strong> role.\


    ![“Users” node showing the user account used to perform the recovery process has been created (if applicable) and assigned the “Full Admin with Access Management role”.](/_images/image-(1967).png "“Users” node showing the user account used to perform the recovery process has been created (if applicable) and assigned the “Full Admin with Access Management role”.")

    \
    If you navigate to the <strong>Events</strong> node, you will see that the <strong>Company Ownership Approved for <</strong>_<strong>user\_name</strong>_<strong>></strong> event confirming the name of the user who performed the recovery process.\


    ![](/_images/image-(1968).png "")

    \
    The previous owner will also receive an email with the subject <strong>Access Recovered to “PMPC\_<</strong>_<strong>company\_name</strong>_<strong>>”</strong>, containing details of who performed the recovery and when.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See [Example Account Recovery Email](../../cloud-reference/cloud-email-reference/example-cloud-account-recovery-email.md) for more details and an example of the email.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>Once you have successfully completed the recovery process, to avoid potential security issues and prevent unwanted re-use of these objects, you should follow the [Deleting an App Registration in Entra ID](../../cloud-reference/entra-id-reference/delete-an-app-registration-in-entra-id.md) process to delete the recovery objects created in your Entra ID.</p>
</blockquote>