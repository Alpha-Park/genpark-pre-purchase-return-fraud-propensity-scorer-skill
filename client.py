class PrePurchaseReturnFraudPropensityScorerClient:
    def score_return_fraud_risk(self, shopper_id='usr_7721', cart_items=[{'sku': 'LUXURY_BAG_01', 'qty': 3, 'price': 1200.00}], historical_return_rate_pct=12.0):
        return {
            'risk_assessment_id': 'rsk_frd_8812',
            'shopper_id': shopper_id,
            'fraud_propensity_score': 0.18,
            'risk_tier': 'LOW_FRAUD_RISK_RELIABLE',
            'wardrobing_suspicion_flag': False,
            'recommended_checkout_policy': 'STANDARD_RETURN_WINDOW_30_DAYS',
            'fraud_evaluation_report_url': 'https://fraud.gorgias.genpark.ai/evals/8812.json'
        }
