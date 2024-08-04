from datetime import datetime
import matplotlib.pyplot as plt

# Чтение файла и преобразование данных в словарь
def read_sales_data(file_path):
    data = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            values = line.strip().split(', ')
            data[f"id_{i+1}"] = {
                'product_name': values[0],
                'quantity': int(values[1]),
                'price': int(values[2]),
                'date': datetime.strptime(values[3], '%Y-%m-%d')
            }
    return data

# Вычисление общей суммы продаж по каждому продукту
def total_sales_per_product(sales_data):
    data = {}

    for product in sales_data.values():
        product_name = product['product_name']
        total_cost = product['quantity'] * product['price']
        if product_name in data:
            data[product_name] += total_cost
        else:
            data[product_name] = total_cost
    return data

# Вычисление общей суммы продаж по дням
def sales_over_time(sales_data):
    data = {}

    for product in sales_data.values():
        date = product['date']
        total_cost = product['quantity'] * product['price']
        if date in data:
            data[date] += total_cost
        else:
            data[date] = total_cost
    return data

def main():

    file_path = 'products.txt'
    data = read_sales_data(file_path)

    # Общие продажи по каждому продукту
    total_sales_of_product = total_sales_per_product(data)
    most_revenue_product = max(total_sales_of_product, key=lambda x: total_sales_of_product[x])
    print(f'Продукт с наибольшей выручкой: {most_revenue_product} ({total_sales_of_product[most_revenue_product]})')

    # Общие продажи по датам
    total_sales_of_date = sales_over_time(data)
    largest_amount_of_sales_day = max(total_sales_of_date, key=lambda x: total_sales_of_date[x])
    print(f'День с наибольшей суммой продаж: {largest_amount_of_sales_day.strftime("%Y-%m-%d")} ({total_sales_of_date[largest_amount_of_sales_day]})')
    data_str_keys = {date.strftime('%Y-%m-%d'): value for date, value in total_sales_of_date.items()}

    # Построение графиков
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))
    
    # Подграфик общей суммы продаж по каждому продукту
    ax1.barh(list(total_sales_of_product.keys()), list(total_sales_of_product.values()))
    ax1.set_ylabel('Название продукта')
    ax1.set_xlabel('Общая сумма продаж')
    ax1.set_title('Общая сумма продаж по каждому продукту')

    # Подписи к столбцам
    for i, value in enumerate(list(total_sales_of_product.values())):
        ax1.text(value, i, f' {value}', va='center', ha='left', fontsize=8)

    # Подграфик общей суммы продаж по дням
    ax2.plot(list(data_str_keys.keys()), list(data_str_keys.values()), marker='o')
    ax2.set_xlabel('Дата')
    ax2.set_ylabel('Общая сумма продаж')
    ax2.set_title('Общая сумма продаж по дням')
    ticks = list(data_str_keys.keys())
    ax2.set_xticks(range(len(ticks)))  
    ax2.set_xticklabels(ticks, rotation=45, ha='right') 
    
    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()

if __name__ == '__main__':
    main()
