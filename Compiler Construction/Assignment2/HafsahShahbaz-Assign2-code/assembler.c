// Hafsah Shahbaz
// 251684784

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *registers[] = {"$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$t8", "$sp"};
const char *decimal_registers[] = {"$8", "$9", "$10", "$11", "$12", "$13", "$14", "$15", "$24", "$29"};
char *registers_machine_code[] = {"01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "11000",
                                  "11101"};

const char *r_opcode[] = {"add", "sub", "and", "or", "slt", "xor"};
char *r_func_machine_code[] = {"100000", "100010", "100100", "100101", "101010", "100110"};

const char *i_opcode[] = {"addi", "andi", "ori", "lw", "sw", "beq"};
char *i_op_machine_code[] = {"001000", "001100", "001101", "100011", "101011", "000100"};

const char *j_opcode[] = {"j"};
char *j_op_machine_code[] = {"000010"};

char *labels[50];
char *label_addr[50];
int label_count = 0;

int displayFile(char *filename)
{
    FILE *fp = fopen(filename, "r");
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file: %s\n", filename);
        return 1;
    }
    char buffer[1024];
    int line_address = 0x00400000;

    while (fgets(buffer, sizeof(buffer), fp) != NULL)
    {
        printf("%s", buffer);
        char *token = strtok(buffer, " :,\n");
        if (strcmp(token, "addi") != 0 && strcmp(token, "andi") != 0 && strcmp(token, "ori") != 0 &&
            strcmp(token, "lw") != 0 && strcmp(token, "sw") != 0 && strcmp(token, "beq") != 0 &&
            strcmp(token, "add") != 0 && strcmp(token, "sub") != 0 && strcmp(token, "and") != 0 &&
            strcmp(token, "or") != 0 && strcmp(token, "slt") != 0 && strcmp(token, "xor") != 0 &&
            strcmp(token, "j") != 0)
        {
            labels[label_count] = strdup(token);
            label_addr[label_count] = malloc(11);
            sprintf(label_addr[label_count], "0x%08x", line_address);
            label_count++;
        }
        line_address += 4;
    }
    fclose(fp);
    return 0;
}

char *binaryToHex(const char *binary)
{
    const char *hexCharacters = "0123456789ABCDEF";

    size_t binaryLen = strlen(binary);

    size_t hexLen = (binaryLen + 3) / 4; // Add 3 to round up to the next multiple of 4

    char *hex = (char *)malloc(hexLen + 1);
    if (hex == NULL)
    {
        fprintf(stderr, "Memory allocation error\n");
        exit(1);
    }

    hex[hexLen] = '\0';
    // Loop group of 4 bits in bin
    for (size_t i = 0; i < hexLen; i++)
    {
        hex[i] = '0';
        // starting index in the binary str
        int start = (int)binaryLen - 4 * (int)(hexLen - i);
        if (start < 0)
        {
            start = 0;
        }
        // Loop through each bit in the group of 4
        for (int j = start; j < (int)binaryLen && j < start + 4; j++)
        {
            hex[i] = (hex[i] << 1) | (binary[j] - '0');
        }
        hex[i] = hexCharacters[hex[i]];
    }
    return hex;
}

char *decimalToBin(int decimal, int num_bits)
{
    if (num_bits <= 0 || num_bits > 32)
    {
        fprintf(stderr, "Invalid number of bits: %d\n", num_bits);
        exit(1);
    }

    if (decimal < 0 || decimal > 67108863)
    {
        fprintf(stderr, "Decimal value out of range: %d\n", decimal);
        exit(1);
    }

    char *binary_imm = (char *)malloc(17 * sizeof(char));
    if (binary_imm == NULL)
    {
        fprintf(stderr, "Memory allocation error\n");
        exit(1);
    }

    for (int i = num_bits - 1; i >= 0; i--)
    {
        binary_imm[i] = (decimal & 1) + '0';
        decimal >>= 1;
    }
    binary_imm[num_bits] = '\0';

    return binary_imm;
}

char *processRType(char *token, char *rd, char *rs, char *rt)
{
    int funcIndex = -1;
    for (int i = 0; i < 6; i++)
    {
        if (strcmp(token, r_opcode[i]) == 0)
        {
            funcIndex = i;
            break;
        }
    }
    if (funcIndex == -1)
    {
        fprintf(stderr, "Unknown R-type instruction: %s\n", token);
        exit(1);
    }

    int rdIndex = -1, rsIndex = -1, rtIndex = -1;
    for (int i = 0; i < 10; i++)
    {
        if (strcmp(rd, registers[i]) == 0 || strcmp(rd, decimal_registers[i]) == 0)
        {
            rdIndex = i;
        }
        if (strcmp(rs, registers[i]) == 0 || strcmp(rs, decimal_registers[i]) == 0)
        {
            rsIndex = i;
        }
        if (strcmp(rt, registers[i]) == 0 || strcmp(rt, decimal_registers[i]) == 0)
        {
            rtIndex = i;
        }
    }

    if (rdIndex == -1 || rsIndex == -1 || rtIndex == -1)
    {
        fprintf(stderr, "Invalid register in R-type instruction\n");
        exit(1);
    }
    char binary[33];
    snprintf(binary, sizeof(binary), "000000%s%s%s00000%s", registers_machine_code[rsIndex], registers_machine_code[rtIndex], registers_machine_code[rdIndex], r_func_machine_code[funcIndex]);

    return binaryToHex(binary);
}

char *processIType(char *token, char *rt, char *rs, char *imm, int line_addr)
{
    int opcodeIndex = -1;
    for (int i = 0; i < 6; i++)
    {
        if (strcmp(token, i_opcode[i]) == 0)
        {
            opcodeIndex = i;
            break;
        }
    }

    if (opcodeIndex == -1)
    {
        fprintf(stderr, "Unknown I-type instruction: %s\n", token);
        exit(1);
    }

    int rtIndex = -1, rsIndex = -1;

    for (int i = 0; i < 10; i++)
    {
        if (strcmp(rt, registers[i]) == 0 || strcmp(rt, decimal_registers[i]) == 0)
        {
            rtIndex = i;
        }
        if (strcmp(rs, registers[i]) == 0 || strcmp(rs, decimal_registers[i]) == 0)
        {
            rsIndex = i;
        }
    }

    if (rtIndex == -1 || rsIndex == -1)
    {
        fprintf(stderr, "Invalid register in I-type instruction\n");
        exit(1);
    }

    // beq $t5, $t6, end
    // andi $t4,$t1,4
    char *addr = NULL;
    char modified_imm[32];

    for (int i = 0; i < label_count; i++)
    {
        if (strcmp(imm, labels[i]) == 0)
        {
            addr = label_addr[i];
            break;
        }
    }
    if (addr != NULL)
    {
        int label_address = (int)strtol(addr, NULL, 16);
        int offset = label_address - line_addr;
        offset /= 4;
        sprintf(modified_imm, "%d", offset);
        imm = modified_imm;
    }
    char *binary_imm = decimalToBin(atoi(imm), 16);

    char binary[33];
    snprintf(binary, sizeof(binary), "%s%s%s%s", i_op_machine_code[opcodeIndex], registers_machine_code[rsIndex], registers_machine_code[rtIndex], binary_imm);

    free(binary_imm);
    return binaryToHex(binary);
}

char *processJType(char *token, char *target)
{
    int opcodeIndex = -1;
    for (int i = 0; i < 1; i++)
    {
        if (strcmp(token, j_opcode[i]) == 0)
        {
            opcodeIndex = i;
            break;
        }
    }
    if (opcodeIndex == -1)
    {
        fprintf(stderr, "Unknown J-type instruction: %s\n", token);
        exit(1);
    }
    char *addr = NULL;
    for (int i = 0; i < sizeof(labels); i++)
    {
        if (strcmp(target, labels[i]) == 0)
        {
            addr = label_addr[i];
            break;
        }
    }
    if (addr == NULL)
    {
        fprintf(stderr, "Label not found: %s\n", target);
        exit(1);
    }

    // convert hex addr(0x00400000) to decimal and divide it by 4
    int decimal_addr = strtol(addr, NULL, 16);

    decimal_addr /= 4;

    // convert that ans to binary string calling *decimalToBin function but make it 26 bit
    char *binary_imm = decimalToBin(decimal_addr, 26);

    if (strlen(binary_imm) > 26)
    {
        fprintf(stderr, "Address overflow: %s\n", addr);
        exit(1);
    }

    char binary[33];
    snprintf(binary, sizeof(binary), "%s%s", j_op_machine_code[opcodeIndex], binary_imm);

    return binaryToHex(binary);
}

void machineCode(char *filename)
{
    FILE *fp = fopen(filename, "r");
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file: %s\n", filename);
        exit(1);
    }

    char buffer[1024];
    int line_address = 0x00400000;
    int pc = 0x00400000;

    while (fgets(buffer, sizeof(buffer), fp) != NULL)
    {
        pc += 4;
        char current_line[sizeof(buffer)];
        strncpy(current_line, buffer, sizeof(buffer) - 1);
        current_line[sizeof(buffer) - 1] = '\0';

        char *token = strtok(buffer, " :,\n");
        if (token == NULL)
            continue;

        char *hex = NULL;

        if (strcmp(token, "add") == 0 || strcmp(token, "sub") == 0 || strcmp(token, "and") == 0 ||
            strcmp(token, "or") == 0 || strcmp(token, "slt") == 0 || strcmp(token, "xor") == 0)
        {
            char *rd = strtok(NULL, " ,\n");
            char *rs = strtok(NULL, " ,\n");
            char *rt = strtok(NULL, " ,\n");

            hex = processRType(token, rd, rs, rt);
        }
        else if (strcmp(token, "addi") == 0 || strcmp(token, "andi") == 0 || strcmp(token, "ori") == 0)
        {
            char *rt = strtok(NULL, " ,\n");
            char *rs = strtok(NULL, " ,\n");
            char *imm = strtok(NULL, " ,\n");
            hex = processIType(token, rt, rs, imm, 0);
        }
        else if (strcmp(token, "beq") == 0)
        {
            char *rs = strtok(NULL, " ,\n");
            char *rt = strtok(NULL, " ,\n");
            char *label = strtok(NULL, " ,\n");
            hex = processIType(token, rt, rs, label, pc);
        }
        else if (strcmp(token, "lw") == 0 || strcmp(token, "sw") == 0)
        {
            char *rt = strtok(NULL, " ,\n");
            char *imm = strtok(NULL, " (),\n");
            char *rs = strtok(NULL, " (),\n");
            // sw $t1,($t2)

            if (imm[0] == '$')
            {
                rs = imm;
                imm = "0";
            }
            // sw $t1,($t2)

            hex = processIType(token, rt, rs, imm, 0);
        }
        else if (strcmp(token, "j") == 0)
        {
            char *target = strtok(NULL, " ,\n");
            hex = processJType(token, target);
        }
        else
        {
            continue;
        }

        printf("0x%08x\t", line_address);
        line_address += 4;

        printf("0x%s", hex);
        // unsigned int machine_code = strtol(hex, NULL, 16);
        // printf("0x%08x", machine_code);
        free(hex);
        printf("\t%s", current_line);
    }
    fclose(fp);
    printf("\n");
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        exit(1);
    }
    printf("\nAssembly language program:\n");
    displayFile(argv[1]);

    printf("\n\nMachine Code:\n");
    machineCode(argv[1]);
}
