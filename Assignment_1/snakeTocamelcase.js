function snakeToCamel(snakeCaseObj) {
    const camelCaseObj = {};
    for (const key in snakeCaseObj) {
        const camelKey = key.replace(/_([a-z])/g, (_, char) => char.toUpperCase());
        camelCaseObj[camelKey] = snakeCaseObj[key];
    }
    return camelCaseObj;
}


const snakeCaseObj = {
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john.doe@example.com"
};

const camelCaseObj = snakeToCamel(snakeCaseObj);
console.log(camelCaseObj);
