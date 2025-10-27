# Cloud User Roles Reference

_Applies to: Patch My PC Cloud_

User roles in the Patch My PC (PMPC) Cloud portal control which administrative tasks a user can perform.

Use the following tables to help you decide which role you should assign a user in Patch My PC Cloud either directly through the Portal or by making them a member of the relevant Entra ID Security Group assigned a role:

<table data-header-hidden><thead><tr><th width="137"></th><th width="100"></th><th width="146"></th></tr></thead><tbody><tr><td><a href="cloud-user-roles-reference.md#app-catalog">App Catalog</a></td><td><a href="cloud-user-roles-reference.md#discovery">Discovery</a></td><td><a href="cloud-user-roles-reference.md#deployments">Deployments</a></td></tr><tr><td><a href="cloud-user-roles-reference.md#events">Events</a></td><td><a href="cloud-user-roles-reference.md#migration">Migration</a></td><td><a href="cloud-user-roles-reference.md#settings">Settings</a></td></tr></tbody></table>

### App Catalog
<div class="table-responsive">

| Functionality    | Read-Only | Custom App Admin | Intune App Admin | Full Admin     | Full Admin with Access Management |
| ---------------- | --------- | ---------------- | ---------------- | -------------- | --------------------------------- |
| Patch My PC Apps | Read      | Read             | Read             | Read           | Read                              |
| Custom Apps      | Read      | Read and Write   | Read             | Read and Write | Read and Write                    |
| Binary Free Apps | Read      | Read             | Read and Write   | Read and Write | Read and Write                    |
</div>

### Deployments

| Read-Only | Custom App Admin | Intune App Admin | Full Admin     | Full Admin with Access Management |
| --------- | ---------------- | ---------------- | -------------- | --------------------------------- |
| Read      | No Access        | Read and Write   | Read and Write | Read and Write                    |

### Discovery

| Read-Only | Custom App Admin | Intune App Admin | Full Admin     | Full Admin with Access Management |
| --------- | ---------------- | ---------------- | -------------- | --------------------------------- |
| Read      | No Access        | Read and Write   | Read and Write | Read and Write                    |

### Events

| Read-Only | Custom App Admin | Intune App Admin | Full Admin | Full Admin with Access Management |
| --------- | ---------------- | ---------------- | ---------- | --------------------------------- |
| Read      | No Access        | Read             | Read       | Read                              |

### Migration

| Read-Only | Custom App Admin | Intune App Admin | Full Admin     | Full Admin with Access Management |
| --------- | ---------------- | ---------------- | -------------- | --------------------------------- |
| Read      | No Access        | No Access        | Read and Write | Read and Write                    |

### Settings

| Functionality           | Read-Only | Custom App Admin | Intune App Admin | Full Admin     | Full Admin with Access Management |
| ----------------------- | --------- | ---------------- | ---------------- | -------------- | --------------------------------- |
| Company                 | Read      | Read             | Read             | Read and Write | Read and Write                    |
| Users                   | Read      | No Access        | No Access        | No Access      | Read and Write                    |
| Environments & Licenses | Read      | Read             | Read and Write   | Read and Write | Read and Write                    |
| Connections             | Read      | Read             | No Access        | Read and Write | Read and Write                    |
| Branding                | Read      | No Access        | Read and Write   | Read and Write | Read and Write                    |
| Notifications           | Read      | No Access        | Read and Write   | Read and Write | Read and Write                    |
| Sync Schedule           | Read      | No Access        | Read and Write   | Read and Write | Read and Write                    |
| Naming Conventions      | Read      | No Access        | Read and Write   | Read and Write | Read and Write                    |
| Templates               | Read      | No Access        | Read and Write   | Read and Write | Read and Write                    |
