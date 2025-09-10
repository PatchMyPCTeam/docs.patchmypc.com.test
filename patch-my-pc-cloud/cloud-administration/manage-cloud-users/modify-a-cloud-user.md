# Modify a Cloud User

_Applies to: Patch My PC Cloud_

Once a user has been successfully created in Patch My PC (PMPC) Cloud, they can be modified in the following ways:

* [Changing the user’s role](modify-a-cloud-user.md#modifying-the-role-assigned-to-a-user)
* [Managing Access Management privileges for a User](modify-a-cloud-user.md#managing-access-management-privileges-for-a-user)

### Modifying the role assigned to a User

To modify the role assigned to a user:

1. Navigate to the <strong>Users</strong> page.
2.  In the <strong>Roles</strong> column, click the down arrow and select the relevant role you want to assign to the user.\
    \
    For example, to change the user’s current role from <strong>Full Admin</strong> to <strong>Custom App Admin</strong>, click the down arrow beside the current role, then choose <strong>Custom App Admin</strong>.\
    \


    ![Selecting the required user role from the list of roles dropdown](/_images/image-(2118).png "Selecting the required user role from the list of roles dropdown")

    \
    The role for the user will be updated and the <strong>Success - Role changed</strong> notification is displayed.\


    ![“Success - Role changed” notification](/_images/image-(1648).png "“Success - Role changed” notification")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>See [User Roles](cloud-user-roles-reference.md) for more information on the user roles available.</p>
</blockquote>

### Managing Access Management privileges for a User

To manage whether a user is granted the <strong>Access Management</strong> privilege:

1. Navigate to the <strong>Users</strong> area.
2.  In the <strong>Roles</strong> column, slide the <strong>Access Management</strong> slider to the right for the user you want to grant this permission.\


    ![Using the slider to grant “Access Management” privileges](/_images/image-(1649).png "Using the slider to grant “Access Management” privileges")

    \
    The <strong>Success - Role changed</strong> notification is displayed.\


    ![The “Success - Role changed&#x22; notification](/_images/image-(1650).png "The “Success - Role changed&#x22; notification")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>To revoke this privilege, slide the <strong>Access Management</strong> slider to the left. If you are the last user in your company with this privilege, you will be unable to revoke it.</p>
<p>If you try revoking it for yourself and there is at least one other user account with this privilege, you will see the following dialog box warning you that if you revoke access management you will be unable to manage user accounts in the portal.</p>
<p>!["Are you sure you want to revoke access management from your account" pop up](/_images/image-(1759).png>)&#x20;</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>As we recommend you have at least two users with Access Management privileges in your environment, if the portal detects you only have one, you will see the following warning message at the top of the portal:</p>
<p><strong>You currently have only one user with Access Management privileges. To prevent access issues in the future, please add a second user with Access Management privileges.</strong></p>
<p>Granting at least two users this privilege will remove this message. Likewise, if revoking Access Management privileges for a user results in only one user in your environment having this privilege, you will see the warning notification again.</p>
</blockquote>