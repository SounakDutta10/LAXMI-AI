def explain_plan(risk_type, investment_dict):
    if risk_type == "Conservative":
        return (
            f"Based on your age, income, and investment goal, we’ve categorized you as a **Conservative Investor**. "
            f"This means your priority is capital protection with steady, low-risk growth.\n\n"
            f"👉 We recommend a combination of:\n"
            f"- **SIP in Large Cap Mutual Funds** like *{investment_dict['SIP'][0]}* for disciplined wealth creation, and\n"
            f"- **Debt Funds** such as *{investment_dict['Debt'][0]}* to provide stability and consistent returns.\n\n"
            f"These options are designed to minimize volatility while helping you reach your financial goals with peace of mind. "
            f"It's a smart and safe route for long-term financial wellness."
        )

    elif risk_type == "Balanced":
        return (
            f"You fall under the **Balanced Investor** category — someone who is open to moderate risk in exchange for higher growth potential.\n\n"
            f"📊 Your recommended plan includes:\n"
            f"- **Hybrid Mutual Funds** like *{investment_dict['MF'][0]}* for diversification between equity and debt, and\n"
            f"- Selective **blue-chip stocks** such as *{investment_dict['Stocks'][0]}* and *{investment_dict['Stocks'][1]}* to fuel long-term returns.\n\n"
            f"This portfolio balances stability with opportunity — perfect for mid- to long-term goals like home ownership or child’s education."
        )

    elif risk_type == "Aggressive":
        return (
            f"As an **Aggressive Investor**, you're comfortable with market volatility and are aiming for maximum returns over the long term.\n\n"
            f"🚀 We suggest:\n"
            f"- A growth-focused equity portfolio including stocks like *{investment_dict['Stocks'][0]}* and *{investment_dict['Stocks'][1]}*, and\n"
            f"- Small allocation in **Crypto** assets like *{investment_dict['Crypto'][0]}* (up to 5%) to tap into emerging trends.\n\n"
            f"This high-risk, high-reward portfolio suits investors with strong financial buffers and long investment horizons. Make sure to monitor regularly!"
        )

    else:
        return (
            f"We're still refining your profile. Please make sure all details are correct, or try again. "
            f"You can also consult a registered financial advisor for personalized strategies."
        )
