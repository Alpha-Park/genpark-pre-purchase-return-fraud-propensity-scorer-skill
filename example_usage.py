from client import PrePurchaseReturnFraudPropensityScorerClient

def main():
    client = PrePurchaseReturnFraudPropensityScorerClient()
    res = client.score_return_fraud_risk('usr_test', [], 5.0)
    print('Return Fraud Scorer: ' + res['risk_assessment_id'] + ' (' + res['risk_tier'] + ')')
    print('Fraud Score: ' + str(res['fraud_propensity_score']) + ' | Policy: ' + res['recommended_checkout_policy'])
    print('Report URL: ' + res['fraud_evaluation_report_url'])

if __name__ == '__main__':
    main()
