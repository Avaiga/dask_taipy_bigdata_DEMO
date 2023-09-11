import time
import pandas as pd
import dask.dataframe as dd

def task1(path_to_original_data: str):
    print("__________________________________________________________")
    print("1. TASK 1: DATA PREPROCESSING AND CUSTOMER SCORING ...")
    start_time = time.perf_counter()  # Start the timer
    
    # Step 1: Read data using Dask
    df = dd.read_csv(path_to_original_data)
    
    # Step 2: Simplify the customer scoring formula
    df['CUSTOMER_SCORE'] = (
        0.5 * df['TotalPurchaseAmount'] / 1000 +
        0.3 * df['NumberOfPurchases'] / 10 +
        0.2 * df['AverageReviewScore']
    )
    
    # Save all customers to a new CSV file
    scored_df = df[["CUSTOMER_SCORE", "TotalPurchaseAmount", "NumberOfPurchases", "TotalPurchaseTime"]]
    
    pd_df = scored_df.compute()

    end_time = time.perf_counter()  # Stop the timer
    execution_time = (end_time - start_time) * 1000  # Calculate the time in milliseconds
    print(f"Time of Execution: {execution_time:.4f} ms")
    
    return pd_df

def task2(scored_df, payment_threshold, score_threshold):
    print("__________________________________________________________")
    print("2. TASK 2: FEATURE ENGINEERING AND SEGMENTATION ...")

    payment_threshold, score_threshold = float(payment_threshold), float(score_threshold)
    start_time = time.perf_counter()  # Start the timer
    
    df = scored_df
    
    # Feature: Indicator if customer's total purchase is above the payment threshold
    df['HighSpender'] = (df['TotalPurchaseAmount'] > payment_threshold).astype(int)
    
    # Feature: Average time between purchases
    df['AverageTimeBetweenPurchases'] = df['TotalPurchaseTime'] / df['NumberOfPurchases']
    
    # Additional computationally intensive features
    df['Interaction1'] = df['TotalPurchaseAmount'] * df['NumberOfPurchases']
    df['Interaction2'] = df['TotalPurchaseTime'] * df['CUSTOMER_SCORE']
    df['PolynomialFeature'] = df['TotalPurchaseAmount'] ** 2
    
    # Segment customers based on the score_threshold
    df['ValueSegment'] = ['High Value' if score > score_threshold else 'Low Value' for score in df['CUSTOMER_SCORE']]
    
    end_time = time.perf_counter()  # Stop the timer
    execution_time = (end_time - start_time) * 1000  # Calculate the time in milliseconds
    print(f"Time of Execution: {execution_time:.4f} ms")
    
    return df

def task3(df: pd.DataFrame, metric):
    print("__________________________________________________________")
    print("3. TASK 3: SEGMENT ANALYSIS ...")
    start_time = time.perf_counter()  # Start the timer
    
    # Detailed analysis for each segment: mean/median of various metrics
    segment_analysis = df.groupby('ValueSegment').agg({
        'CUSTOMER_SCORE': metric,
        'TotalPurchaseAmount': metric,
        'NumberOfPurchases': metric,
        'TotalPurchaseTime': metric,
        'HighSpender': 'sum',  # Total number of high spenders in each segment
        'AverageTimeBetweenPurchases': metric
    }).reset_index()
    
    end_time = time.perf_counter()  # Stop the timer
    execution_time = (end_time - start_time) * 1000  # Calculate the time in milliseconds
    print(f"Time of Execution: {execution_time:.4f} ms")
    
    return segment_analysis

def task4(df: pd.DataFrame, segment_analysis: pd.DataFrame, summary_statistic_type: str):
    print("__________________________________________________________")
    print("4. TASK 4: ADDITIONAL ANALYSIS BASED ON SEGMENT ANALYSIS ...")
    start_time = time.perf_counter()  # Start the timer

    # Filter out the High Value customers
    high_value_customers = df[df['ValueSegment'] == 'High Value']
    
    # Use summary_statistic_type to calculate different types of summary statistics
    if summary_statistic_type == 'mean':
        average_purchase_high_value = high_value_customers['TotalPurchaseAmount'].mean()
    elif summary_statistic_type == 'median':
        average_purchase_high_value = high_value_customers['TotalPurchaseAmount'].median()
    elif summary_statistic_type == 'max':
        average_purchase_high_value = high_value_customers['TotalPurchaseAmount'].max()
    elif summary_statistic_type == 'min':
        average_purchase_high_value = high_value_customers['TotalPurchaseAmount'].min()
    
    median_score_high_value = high_value_customers['CUSTOMER_SCORE'].median()
    
    # Fetch the summary statistic for 'TotalPurchaseAmount' for High Value customers from segment_analysis
    segment_statistic_high_value = segment_analysis.loc[segment_analysis['ValueSegment'] == 'High Value', 'TotalPurchaseAmount'].values[0]

    # Create a DataFrame to hold the results
    result_df = pd.DataFrame({
        'SummaryStatisticType': [summary_statistic_type],
        'AveragePurchaseHighValue': [average_purchase_high_value],
        'MedianScoreHighValue': [median_score_high_value],
        'SegmentAnalysisHighValue': [segment_statistic_high_value]
    })

    end_time = time.perf_counter()  # Stop the timer
    execution_time = (end_time - start_time) * 1000  # Calculate the time in milliseconds
    print(f"Time of Execution: {execution_time:.4f} ms")

    return result_df




if __name__ == "__main__":

    t1 = task1("data/SMALL_amazon_customers_data.csv")

    t2 = task2(t1, 1500, 1.5)

    t3 = task3(t2, "mean")

    t4 = task4(t2, t3, "mean")



    print(t4)

