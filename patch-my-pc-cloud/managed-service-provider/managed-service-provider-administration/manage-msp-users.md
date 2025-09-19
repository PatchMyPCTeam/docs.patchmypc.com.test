# Manage MSP Users

_Applies to: Patch My PC Cloud_

Managed Service Providers (MSPs) can manage users in both their own Patch My PC (PMPC) Cloud company and any child companies they manage using the standard [Manage Users](../../cloud-administration/manage-cloud-users/) processes.

This includes inviting users of the child company to their PMPC Cloud portal.

Any users created in the MSP parent company will automatically be assigned the same role in any child company, as child companies inherit user roles from the parent company.

For example, if a user is created in the parent company and assigned the **Full Admin with Access Management** role, they will have the same role permissions in any child companies.

> **Note**
>
> Any accounts created in the parent company will not appear in any child companies.
>
> Also, if the MSP creates a new child company, no users are automatically created in the child company.

Once an MSP has created a child company, users can request access to it by attempting to sign in to the portal using an email address that matches the one used to onboard the child company.

The parent company admin will need to navigate to the **Users** node on the relevant child company to approve or reject any access requests.

> **Note**
>
> If the child company does not have any existing admin users, the access request email will be sent to the admin of the parent company. See \[Managing MSP Notifications]\(manage-msp-notifications.md) for more details on how notifications, including emails are handled in MSP companies.

The following table lists the levels of access MSP Customers have to objects within the PMPC Cloud Portal, depending on which role you have assigned them (either directly or through them being a member of an Entra ID Security Group assigned a role).

| Read-Only | Custom App Admin | Intune App Admin | Full Admin     | Full Admin with Access Management |
| --------- | ---------------- | ---------------- | -------------- | --------------------------------- |
| Read      | Read             | Read             | Read and Write | Read and Write                    |
