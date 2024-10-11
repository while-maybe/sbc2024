// PrivacyPrettyPrinter!

/*
The program will mask digits and characters from phone numbers and E-mails for privacy.
Given an array of dicts with name, phone and e-mail it will manipulate the string to ensure that names and E-mails are aligned to the right, that it fits on the table cell and if the length exceeds the limit, it will shorten Names and E-mails as follows:
- Names: If the given name doesn't fit, it will abbreviate the firstName. If it still doesn't fit, it will show as much of the real surname as possible but will end it with "..."
- Emails: After an E-mail is masked, we show the first 2 (real) chars of the address and the maximum possible number of ending chars.

Expected result:
------------------------------------------------------------
|      Name      |    Phone    |         Email             |
------------------------------------------------------------
| R AVeryVery... | 01******826 | ri*********@microsoft.com |
|  D Oakenshield | 03******893 |             de**@mail.com |
|     John Smith | 07******829 | jo***********@hotmail.com |
------------------------------------------------------------

The exercise asked for at least 3 string methods, so I used 13:
.at()
.repeat()
.split()
.trim()
.charAt()
.indexOf()
.toLowerCase()
.toUpperCase()
.concat()
.slice()
.substr()
.padStart()
.padEnd()

Note: the code if far from optimal but the below were chosen to cram a lot string methods to demonstrate their use.
*/


const people = [
    {
        name: "     Richard aVeryVeryLongsurname   ",
        phone: "01793223826",
        email: "richard_the_viper@microsoft.com"
    },
    {
        name: "Deborah oakenshield",
        phone: "03305376893   ",
        email: "    debz@mail.com       "
    },
    {
        name: "John Smith",
        phone: "07793523829",
        email: "johnsmith2000@hotmail.com"
    }
];

const maxNameLength = 14;
const maxPhoneLength = 11;
const maxEmailLength = 25;

function prettyPrint(people) {
    const fullLine = "-".repeat(60);
    //                12345678901234   12345678901   1234567890123456789012345
    const header = `|      Name      |    Phone    |         Email             |`;
    console.log(`${fullLine}\n${header}\n${fullLine}`);

    for (person of people) {
        // trims leading and trailing whitespaces from name, phone and email before passing these to the function printOneLine()
        console.log(printOneLine(person.name.trim(), person.phone.trim(), person.email.trim()));
    }

    console.log(fullLine);
}

function printOneLine(name, phone, email) {
    let makeShort = function(name) {
        // splits the provided name into an array of strings
        let names = name.split(" ");
        // extracts the first char of the first name and converts to upper case
        const initial = names[0].charAt(0).toUpperCase();
        // grabs the surname
        let surName = names.at(-1);
        // if the length of the surname - initial(1) - space (1) is bigger than the "cell width", grab the first 9 chars of the surname and adds "..." to it so the surname total length becomes 12
        surName = surName.length > maxNameLength - 2 ? surName.slice(0, 9).concat("...") : surName;
        // reuses the variable and converts first letter of surname to upper case
        surName = surName
            .charAt(0)
            .toUpperCase()
            .concat(surName
                .slice(1));
        // add leading spaces if length of name is below maxNameLength
        return `${initial} ${surName}`.padStart(maxNameLength, " ");
    }

    let makeLong = function(name, length) {
        // if the total length is below maxNameLength add leading spaces
        return name.padStart(length, " ");
    }

    function maskNumber(phone) {
        // masks the middle 6 digits of the given number and ads the remaining from position 7 onwards - 0 based index
        return phone
            .slice(0, 2)
            // add 8x "*" after the first 2 chars
            .padEnd(8, "*")
            .concat(phone
                .slice(8));
    }

    function maskEmail(email) {
        const atSymIndex = email.indexOf("@");

        return email.toLowerCase()
            .slice(0, 2)
            .padEnd(atSymIndex, "*")
            .concat(email
                .slice(atSymIndex));
    }

    function makeShortEmail(email) {
        // extracts first 2 chars from email and adds the number of remaining characters to fill the table cell starting from the end of the existing email address minus 2 chars (the ones we keep at the beginning)
        return email.substr(0, 2).concat(email.substr(-maxEmailLength + 2));
    }

    const prettyName = name.length >= maxNameLength ? makeShort(name) : makeLong(name, maxNameLength);
    const prettyEmail = email.length >= maxEmailLength ? makeShortEmail(maskEmail(email)) : makeLong(maskEmail(email), maxEmailLength);
    
    return `| ${prettyName} | ${maskNumber(phone)} | ${prettyEmail} |`;
};


prettyPrint(people)
