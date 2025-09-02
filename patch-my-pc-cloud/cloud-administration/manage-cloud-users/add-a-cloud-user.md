# Add a Cloud User

_Applies to: Patch My PC Cloud_

Users can be added to the PMPC Cloud portal by:

* [Invitation from an Administrator](add-a-cloud-user.md#invitation-from-an-administrator)
* [Users requesting access](add-a-cloud-user.md#users-requesting-access)

{% hint style="info" %}
**Note**

Users can also access the portal if they are members of one or more Entra ID Security Groups that have been added to the portal.

If a user has been added directly to the portal using the processes detailed in this article and they are also a member of an Entra ID Security Group that is granted access to the same PMPC Cloud company, they will appear both under the **Users** tab and a member of the relevant Entra ID Security Group(s) when following the [View an Entra ID Group's Membership](using-entra-id-security-groups-in-cloud/view-an-entra-id-groups-membership-in-cloud.md) process.
{% endhint %}

### Invitation from an Administrator

To invite a new user to the PMPC Cloud portal:

1. Navigate to **Settings | Users**.
2.  Click **Invite User** in the header.\


    ![](/_images/image-(722 "").png "")
3.  On the **Invite User** screen, enter the user’s details.\


    ![](/_images/image-(2119 "").png "")

{% hint style="warning" %}
**Important**

The email address you enter must already have an Entra ID account associated with it. If it does not, that user cannot sign into PMPC Cloud.
{% endhint %}

4. Under the **Role** section, click the relevant option for the role you want to assign in the PMPC Cloud portal.

{% hint style="info" %}
**Note**

See [User Roles](cloud-user-roles-reference.md) for details of the available roles and which actions they can perform.
{% endhint %}

![](/_images/image-(2120 "").png "")

{% hint style="success" %}
**Tip**

Use the tooltips beside each role to gain a quick overview of the role and it's capabilities.
{% endhint %}

5.  Click **Invite**.\
    \


    ![](/_images/image-(2122 "").png "")

The **Success - Invitation sent** notification is displayed.

![](/_images/image-(725 "").png "")

The user will receive an email from the [noreply@patchmypc.com](mailto:noreply@patchmypc.com) mailbox with the subject **You are invited to&#x20;**_**\<company\_name>**_.

{% hint style="info" %}
**Note:**

See [Example Invitation email](../../cloud-reference/cloud-email-reference/example-cloud-invitation-email.md) to see an example of the email.
{% endhint %}

The invitation and its details are shown on the **Invitations** tab, which includes any previously created outstanding invitations that are still valid.

![](/_images/image-(728 "").png "")

{% hint style="info" %}
**Note**

Invitations are valid for 60 days from the date of issue. If the user does not accept the invitation within this time period, it will expire, and the user will need to be re-invited.

Users should follow the [Accepting an Invitation](manage-cloud-invitations/accept-a-cloud-invitation.md) process to onboard to the PMPC Cloud portal.
{% endhint %}

### Users requesting access

When a user from the same company who has not been set up on your company's PMPC Cloud portal tries to sign in, they will see the **Select the Company You Want to Sign In To** screen.

![](/_images/image-(1378 "").png "")

To join your company, they should click **Request Access** beside your company.

![](/_images/image-(1379 "").png "")

The **Request Access to join&#x20;**_**\<company\_name>**_ popup appears.

![](/_images/image-(616 "").png "")&#x22; popup">

The user should enter an optional **Reason for Request** then click **Submit**.&#x20;

The **Request Access** text changes to **Renotify** and the **Success - Access request sent** notification is shown.

![](/_images/image-(617 "").png "")

Any users with the **Full Admin** role in your PMPC Cloud portal will receive an email containing the user’s details and which company they have requested access to. The email is sent from the [noreply@patchmypc.com](mailto:noreply@patchmypc.com) mailbox with the subject **Access Request&#x20;**_**\<your\_company\_name>**_.

{% hint style="info" %}
**Note**

See [Example Access Request email](../../cloud-reference/cloud-email-reference/example-cloud-access-request-email.md) to see an example of the email.
{% endhint %}

{% hint style="warning" %}
**Important**

The user cannot access the PMPC Cloud portal until their request is approved. See [Managing Access Requests](manage-cloud-access-requests/) for more details.
{% endhint %}
