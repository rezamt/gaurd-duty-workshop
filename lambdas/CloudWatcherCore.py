import boto3
import json

'''
https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_unauthorized.html
'''
criticalAccount = [
    'UnauthorizedAccess:EC2/MetadataDNSRebind',
    'UnauthorizedAccess:IAMUser/TorIPCaller',
    'UnauthorizedAccess:IAMUser/MaliciousIPCaller.Custom',
    'UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B',
    'UnauthorizedAccess:IAMUser/MaliciousIPCaller',
    'UnauthorizedAccess:EC2/TorIPCaller',
    'UnauthorizedAccess:EC2/MaliciousIPCaller.Custom',
    'UnauthorizedAccess:EC2/SSHBruteForce',
    'UnauthorizedAccess:EC2/RDPBruteForce',
    'UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration',
    'UnauthorizedAccess:IAMUser/ConsoleLogin',
    'UnauthorizedAccess:EC2/TorClient',
    'UnauthorizedAccess:EC2/TorRelay',
]
'''
https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_trojan.html
'''
informationalAccount = ['Trojan:EC2/BlackholeTraffic',
                        'Trojan:EC2/DropPoint',
                        'Trojan:EC2/BlackholeTraffic!DNS',
                        'Trojan:EC2/DriveBySourceTraffic!DNS',
                        'Trojan:EC2/DropPoint!DNS',
                        'Trojan:EC2/DGADomainRequest.B',
                        'Trojan:EC2/DGADomainRequest.C!DNS',
                        'Trojan:EC2/DNSDataExfiltration',
                        'Trojan:EC2/PhishingDomainRequest!DNS']

'''
https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_crypto.html
'''
criticalInfrastructure = [
    'CryptoCurrency:EC2/BitcoinTool.B!DNS',
    'CryptoCurrency:EC2/BitcoinTool.B'
]

def ParserCore(event, eventType):
    client=boto3.client('lambda')
    result = "Not currently a Coded Issue"

    for e in criticalAccount:
        # print eventType
        # print e
        if str(eventType) == str(e):
            result = "EmergencyActionAccount"
            return result

    for e in informationalAccount:
        # print eventType
        # print e
        if str(eventType) == str(e):
            result = "InformationalAccount"
            return result


    for e in criticalInfrastructure:
        # print eventType
        # print e
        if str(eventType) == str(e):
            result = "CriticalInfrastructure"
            return result

def lambda_handler(event, context):
    print("event: {}".formatter(json.dump(event)))
    eventType= event["type"]
    evaluation = ParserCore(event, eventType)
    print("Evaluation: ", evaluation)



