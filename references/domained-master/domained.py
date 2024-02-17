from tld import get_tld

def domain_extract():
    domainName = input("Enter a URL: ")
    sub_domain = False
    domain_data = get_tld(domainName, as_object=True, fix_protocol=True)
    name = domain_data.domain
    ext = domain_data.tld
    sub = domain_data.subdomain
    if sub != '':
        sub_domain = True
    
    return {
        'sub_domain': sub_domain,
        'full_domain': domainName,
        'name': name,
        'ext': ext
    }

result = domain_extract()
print(result)