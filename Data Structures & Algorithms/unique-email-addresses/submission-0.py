class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            
            # 1. Remove everything after the first '+' in the local name
            local_name = local_name.split('+')[0]

            # 2. Remove all periods '.' from the local name
            local_name = local_name.replace('.', '')

            # 3. Add the normalized email (or tuple) to the set
            unique_emails.add(local_name + '@' + domain_name)

        return len(unique_emails)