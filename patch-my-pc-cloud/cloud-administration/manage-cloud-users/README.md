# Manage Cloud Users

_Applies to: Patch My PC Cloud_

A _user_ needs an account to sign in and use any of the features of Patch My PC (PMPC) Cloud.

There are two ways to grant access:

* Directly through the PMPC Portal as detailed below.
* By using Entra ID Security Groups.

All user account-related tasks are performed from the <strong>Users</strong> node of the PMPC portal, which is accessed by:

1. Sign in to the PMPC portal [https://portal.patchmypc.com/](https://portal.patchmypc.com/)
2.  Navigate to  <strong>Settings | Users</strong>.\


    ![Navigating to “Settings | Users”](/_images/image-(286).png "Navigating to “Settings | Users”")

The <strong>Users</strong> page is then displayed, allowing you to complete the following tasks:

* [Add a User](add-a-cloud-user.md)
* [Modify a User](modify-a-cloud-user.md)
* [Delete a User](delete-a-cloud-user.md)

![“Users” page](/_images/image-(287).png "“Users” page")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>When you first set up a PMPC Cloud company, the user creating the company is automatically assigned the <strong>Full Admin with Access Management</strong> role. To avoid access issues (such as this user leaving your company and not passing on their credentials/setting up another user with this role), we recommend either:</p>
<p>* [Adding a second user](add-a-cloud-user.md) and assigning them this role.</p>
<p>* [Adding an Entra ID group](using-entra-id-security-groups-in-cloud/add-an-entra-id-group-to-cloud.md) and assigning it the <strong>Full Admin with Access Management</strong> role.</p>
<p>Once you’ve done this, we recommend you use Entra ID security groups to manage any additional users who need to have access to your PMPC Cloud company.</p>
<p>You will see the banner at the top of the portal warning you only have one user with Access Management privileges until you create at least another user or grant an Entra ID Security Group this privilege.</p>
</blockquote>