# “Unable to change the role of this group as it was not found in Entra ID” error in Cloud

_Applies to: Patch My PC Cloud_

### SYMPTOMS

I am trying to change the role assigned to an Entra ID Security Group in the Patch My PC (PMPC) Cloud portal, but I get the following error:

**Error - Unable to change the role of this group as it was not found in Entra ID**

![&#x22;Unable to change the role of this group as it was not found in Entra ID&#x22; error](../../../_images/image%20%282292%29.png%20"&#x22;Unable%20to%20change%20the%20role%20of%20this%20group%20as%20it%20was%20not%20found%20in%20Entra%20ID&#x22;%20error")

### CAUSE

This error is caused if the Entra ID Security Group has been deleted in Entra ID. If you refresh the portal, you will see the **GROUP WAS DELETED ON AZURE**  message and you can only delete the group.

![“Group role was deleted on Azure” error](../../../_images/image%20%28348%29.png%20"\"Group%20role%20was%20deleted%20on%20Azure\"%20error")

### RESOLUTION

To resolve this issue:

1. Delete the existing group from the portal. Just recreating the group in Entra ID won’t work, as the group will have a different Entra ID than the existing one in the portal.
2. Recreate the group in Entra ID with the relevant members.
3. Add the group to the portal.
