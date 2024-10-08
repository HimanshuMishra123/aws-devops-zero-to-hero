### Granting EKS Cluster Access to a New Person

To give a new person access to an Amazon EKS cluster, you need to update both the IAM permissions and the Kubernetes Role-based Access Control (RBAC) settings. Here's how you can do it step-by-step:

### Steps to Grant Access

#### 1. **Update the AWS IAM Role or User Permissions:**

   1.1 **Create or Update IAM User/Role:**
   - If the new person doesn't already have an AWS IAM user or role, create one.
     - Go to **IAM** > **Users** > **Add User**.
     - Attach the necessary permissions for EKS, such as:
       ```json
       {
         "Effect": "Allow",
         "Action": [
           "eks:DescribeCluster",
           "eks:ListClusters"
         ],
         "Resource": "*"
       }
       ```

   1.2 **Attach Permissions for EKS Cluster:**
   - Ensure the IAM user/role has permissions for interacting with the cluster. Typically, they need access to `eks:DescribeCluster`, and potentially other actions like `eks:ListClusters`, `eks:CreateNodegroup`, etc.

#### 2. **Update EKS Cluster ConfigMap for RBAC:**

   2.1 **Edit aws-auth ConfigMap:**
   - To give the new person access to the EKS cluster, update the `aws-auth` ConfigMap, which maps IAM users or roles to Kubernetes RBAC.
   - Use `kubectl` to edit the `aws-auth` ConfigMap:
     ```bash
     kubectl edit configmap aws-auth -n kube-system
     ```
   - Add a new `mapUsers` or `mapRoles` entry for the person you are granting access to.

   **Example for an IAM User:**
   ```yaml
   mapUsers: |
     - userarn: arn:aws:iam::<account-id>:user/<username>
       username: <username>
       groups:
         - system:masters
   ```

   **Example for an IAM Role:**
   ```yaml
   mapRoles: |
     - rolearn: arn:aws:iam::<account-id>:role/<rolename>
       username: <username>
       groups:
         - system:masters
   ```

   2.2 **Save and Apply the ConfigMap:**
   - After updating, save the changes, and the person should have the specified access to the cluster.

#### 3. **Verify Access:**

   3.1 **Update Kubeconfig:**
   - Share the kubeconfig with the new user, or they can generate it with the AWS CLI:
     ```bash
     aws eks update-kubeconfig --name <cluster-name> --region <region-name> --role-arn arn:aws:iam::<account-id>:role/<rolename>
     ```

   3.2 **Test Access:**
   - The new person can now verify their access to the cluster by running `kubectl get nodes` or another test command to ensure the permissions are correct.

### Use Case
This setup is common when adding new team members to a Kubernetes cluster running on EKS, ensuring they have the necessary permissions to view or manage resources while maintaining security through IAM and RBAC.

If you have any further questions or need more details, feel free to ask!
