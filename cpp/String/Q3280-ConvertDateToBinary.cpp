class Solution {
public:
    string convertDateToBinary(string date) {
        string converted_date = "";

        vector<string> split_arr = split(date, '-');

        for (const auto& s: split_arr) {
            int num = stoi(s);
            bitset<16> binary(num);
            string bin_str = binary.to_string();
            size_t first_one = bin_str.find_first_not_of('0');

            if (first_one != string::npos) {
                bin_str = bin_str.substr(first_one);
            } else {
                bin_str = "0";
            }

            converted_date += bin_str + "-";
        }

        if (!converted_date.empty()) {
            converted_date.pop_back();
        }

        return converted_date;
    }

    vector<string> split(const string& str, char delimiter) {
        vector<string> result;
        stringstream ss(str);
        string token;

        while (getline(ss, token, delimiter)) {
            result.push_back(token);
        }
        return result;
    }
};