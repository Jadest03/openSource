def read_data(filename):
    f = open(filename, "r")
    data = []
    for line in f.readlines(): # 한 줄씩 읽어오기
        if line.strip("\n") != "# midterm (max 125), final (max 100)":
            data.append([int(word) for word in line.split(",")]) # 한 배열을 ,로 구분하여 int형으로 저장
    f.close()
    return data


def calc_weighted_average(data_2d, weight):
    average = []
    for data in data_2d:
        value = round(data[0] * weight[0] + data[1] * weight[1], 2)
        value = format(value, ".3f")
        average.append(float(value))

    return average


def analyze_data(data_1d):
    # 길이
    length = len(data_1d)

    # 평균
    sum = 0
    for i in data_1d:
        sum += i
    mean = sum / length

    # 분산
    dev = 0
    for i in data_1d:
        dev += (mean - i) ** 2
    var = dev / length

    # 중앙값
    data_1d.sort()
    median = data_1d[int(length / 2)]

    return mean, var, median, min(data_1d), max(data_1d)


if __name__ == "__main__":
    data = read_data("lab02/data/class_score_en.csv")

    if data and len(data[0]) == 2:  # Check 'data' is valid
        average = calc_weighted_average(data, [40 / 125, 60 / 100])

        # Write the analysis report as a markdown file
        with open("lab02/lab02.md", "w") as report:
            report.write("### Individual Score\n\n")
            report.write("| Midterm | Final | Total |\n")
            report.write("| ------- | ----- | ----- |\n")
            for (m_score, f_score), a_score in zip(data, average):
                report.write(f"| {m_score} | {f_score} | {a_score:.3f} |\n")
            report.write("\n\n\n")

            report.write("### Examination Analysis\n")
            data_columns = {
                "Midterm": [m_score for m_score, _ in data],
                "Final": [f_score for _, f_score in data],
                "Average": average,
            }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f"* {name}\n")
                report.write(f"  * Mean: **{mean:.3f}**\n")
                report.write(f"  * Variance: {var:.3f}\n")
                report.write(f"  * Median: **{median:.3f}**\n")
                report.write(f"  * Min/Max: ({min_:.3f}, {max_:.3f})\n")
