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


    ![](../../../_images/image%20%28722%29.png%20"")
3.  On the **Invite User** screen, enter the user’s details.\


    ![Complete the details of the user you are inviting](../../../_images/image%20%282119%29.png%20"Complete%20the%20details%20of%20the%20user%20you%20are%20inviting")

{% hint style="warning" %}
**Important**

The email address you enter must already have an Entra ID account associated with it. If it does not, that user cannot sign into PMPC Cloud.
{% endhint %}

4. Under the **Role** section, click the relevant option for the role you want to assign in the PMPC Cloud portal.

{% hint style="info" %}
**Note**

See [User Roles](cloud-user-roles-reference.md) for details of the available roles and which actions they can perform.
{% endhint %}

![Choosing which role to assign this user](../../../_images/image%20%282120%29.png%20"Choosing%20which%20role%20to%20assign%20this%20user")

{% hint style="success" %}
**Tip**

Use the tooltips beside each role to gain a quick overview of the role and it's capabilities.
{% endhint %}

5.  Click **Invite**.\
    \


    ![Clicking &#x22;Invite&#x22; to send the invitation](../../../_images/image%20%282122%29.png%20"Clicking%20&#x22;Invite&#x22;%20to%20send%20the%20invitation")

The **Success - Invitation sent** notification is displayed.

![&#x22;Success - Invitation sent&#x22; notification](../../../_images/image%20%28725%29.png%20"&#x22;Success%20-%20Invitation%20sent&#x22;%20notification")

The user will receive an email from the [noreply@patchmypc.com](mailto:noreply@patchmypc.com) mailbox with the subject **You are invited to&#x20;**_**\<company\_name>**_.

{% hint style="info" %}
**Note:**

See [Example Invitation email](../../cloud-reference/cloud-email-reference/example-cloud-invitation-email.md) to see an example of the email.
{% endhint %}

The invitation and its details are shown on the **Invitations** tab, which includes any previously created outstanding invitations that are still valid.

![“Invitations” tab showing valid, outstanding user invitations](../../../_images/image%20%28728%29.png%20"\"Invitations\"%20tab%20showing%20valid,%20outstanding%20user%20invitations")

{% hint style="info" %}
**Note**

Invitations are valid for 60 days from the date of issue. If the user does not accept the invitation within this time period, it will expire, and the user will need to be re-invited.

Users should follow the [Accepting an Invitation](manage-cloud-invitations/accept-a-cloud-invitation.md) process to onboard to the PMPC Cloud portal.
{% endhint %}

### Users requesting access

When a user from the same company who has not been set up on your company's PMPC Cloud portal tries to sign in, they will see the **Select the Company You Want to Sign In To** screen.

![“Select the Company You Want to Sign In To” screen](../../../_images/image%20%281378%29.png%20"\"Select%20the%20Company%20You%20Want%20to%20Sign%20In%20To\"%20screen")

To join your company, they should click **Request Access** beside your company.

![Users should click “Request Access” beside your company to join it](../../../_images/image%20%281379%29.png%20"Users%20should%20click%20\"Request%20Access\"%20beside%20your%20company%20to%20join%20it")

The **Request Access to join&#x20;**_**\<company\_name>**_ popup appears.

![](../../../_images/image%20%28616%29.png%20"")

The user should enter an optional **Reason for Request** then click **Submit**.&#x20;

The **Request Access** text changes to **Renotify** and the **Success - Access request sent** notification is shown.

![The “Success – Request sent” notification is displayed](../../../_images/image%20%28617%29.png%20"The%20\"Success%20–%20Request%20sent\"%20notification%20is%20displayed")

Any users with the **Full Admin** role in your PMPC Cloud portal will receive an email containing the user’s details and which company they have requested access to. The email is sent from the [noreply@patchmypc.com](mailto:noreply@patchmypc.com) mailbox with the subject **Access Request&#x20;**_**\<your\_company\_name>**_.

{% hint style="info" %}
**Note**

See [Example Access Request email](../../cloud-reference/cloud-email-reference/example-cloud-access-request-email.md) to see an example of the email.
{% endhint %}

{% hint style="warning" %}
**Important**

The user cannot access the PMPC Cloud portal until their request is approved. See [Managing Access Requests](manage-cloud-access-requests/) for more details.
{% endhint %}
